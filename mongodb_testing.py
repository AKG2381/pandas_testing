import pymongo
from datetime import datetime
from pprint import pprint

from pymongo import MongoClient

# Replace the URI string with your MongoDB connection string
client = MongoClient("mongodb://127.0.0.1:27017")
db = client["my_testing_db"]


# Access a collection
aj_sales = db["sales_ajeet"]
aj_products = db["products_ajeet"]


match_stage = {
    "$match": {
        "date": {
            "$gte": datetime(2024, 10, 1)
        }
    }
}

group_stage = {
    "$group": {
        "_id": "$product_id",
        "totalRevenue": {
            "$sum": {
                "$multiply": ["$quantity", "$price"]
            }
        }
    }
}

sort_stage = {
    "$sort": {
        "totalRevenue": -1
    }
}


print(list(aj_sales.aggregate([match_stage, group_stage, sort_stage])))

"""
Step 1: $lookup to Join sales with products
We want to include product details (like product_name and category) from the products collection in each sale document from the sales collection.

{ 
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "_id",
    as: "product_info"
  }
}
This will add an array field product_info with the corresponding product details in each sale document.


Step 2: $unwind the product_info Array
To make product_info fields accessible as direct fields, we use $unwind:

{ $unwind: "$product_info" }


Step 3: $project to Reshape the Output
We use $project to select specific fields and create calculated fields. Here, we’ll compute the total_cost for each sale (quantity * price) and
include only necessary fields:

{ 
  $project: {
    _id: 1,
    product_id: 1,
    date: 1,
    quantity: 1,
    price: 1,
    total_cost: { $multiply: ["$quantity", "$price"] },
    product_name: "$product_info.product_name",
    category: "$product_info.category"
  }
}

Step 4: $group to Aggregate Total Sales by Product
Now, we’ll group by product_id and sum total_cost to get total_sales for each product:

{ 
  $group: {
    _id: { product_id: "$product_id", product_name: "$product_name" },
    total_sales: { $sum: "$total_cost" }
  }
}


Step 5: $bucket to Categorize Total Sales into Ranges
We can use $bucket to categorize products by their total_sales values, dividing them 
into different ranges (e.g., "Low", "Medium", "High").
{ 
  $bucket: {
    groupBy: "$total_sales",
    boundaries: [0, 50, 100, 150, 200],
    default: "High",
    output: {
      products_in_range: { $push: "$_id.product_name" },
      total_sales: { $sum: "$total_sales" }
    }
  }
}
This will bucket total_sales into ranges like [0, 50), [50, 100), etc., 
and place products within these ranges.

"""

data = aj_sales.aggregate([
    { 
      "$lookup": {
        'from': "products_ajeet",
        'localField': "product_id",
        'foreignField': "_id",
        'as': "product_info"
      }
    }
    ,
    { '$unwind': "$product_info" }
    ,
    { 
      '$project': {
        '_id': 1,
        'product_id': 1,
        'date': 1,
        'quantity': 1,
        'price': 1,
        'total_cost': { '$multiply': ["$quantity", "$price"] },
        'product_name': "$product_info.product_name",
        'category': "$product_info.category"
      }
    }
    ,
    { 
      '$group': {
        '_id': { 'product_id': "$product_id", 'product_name': "$product_name" },
        'total_sales': { '$sum': "$total_cost" }
      }
    }
    ,
    { 
      '$bucket': {
        'groupBy': "$total_sales",
        'boundaries': [0, 50, 100, 150, 200],
        'default': "High",
        'output': {
          'products_in_range': { '$push': "$_id.product_name" },
          'total_sales': { '$sum': "$total_sales" }
        }
      }
    }
])

pprint(list(data))