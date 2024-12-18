"""
Problem: You have two DataFrames, df1 and df2, with the following columns:

df1: product_id, sales, category
df2: product_id, category, discount
You need to merge the two DataFrames on both product_id and category columns. After merging, 
you should get a DataFrame with columns: product_id, sales, category, and discount.

Solution Steps:
Use merge() to join the two DataFrames on both product_id and category columns.
Ensure that the merge is done correctly and both columns are used as keys.
"""

import pandas as pd

# Sample data for df1
data1 = {
    'product_id': [1, 2, 3, 4],
    'sales': [100, 200, 300, 400],
    'category': ['A', 'B', 'A', 'B']
}
df1 = pd.DataFrame(data1)

# Sample data for df2
data2 = {
    'product_id': [1, 2, 3, 4],
    'category': ['A', 'B', 'A', 'B'],
    'discount': [10, 15, 20, 25]
}
df2 = pd.DataFrame(data2)

# Display the DataFrames
print("df1:")
print(df1)
print("\ndf2:")
print(df2)


# Merge the DataFrames on both 'product_id' and 'category'
merged_df = pd.merge(df1, df2, on=['product_id', 'category'])

# Display the merged DataFrame
print("\nMerged DataFrame:")
print(merged_df)



"""
Problem: You have two DataFrames, df1 and df2, with the following columns:

df1: product_id, sales
df2: product_id, category
You need to:

Merge df1 and df2 on the product_id column to combine sales data with category information.
After merging, calculate the total sales for each category.

Solution Steps:
Use merge() to join the DataFrames on the product_id column.
Use groupby() to calculate the total sales for each category.

"""


import pandas as pd

# df1: Sales data
data1 = {
    'product_id': [1, 2, 3, 4],
    'sales': [100, 200, 300, 400]
}
df1 = pd.DataFrame(data1)

# df2: Category data
data2 = {
    'product_id': [1, 2, 3, 4],
    'category': ['A', 'B', 'A', 'B']
}
df2 = pd.DataFrame(data2)

# Display the DataFrames
print("df1:")
print(df1)
print("\ndf2:")
print(df2)

# Merge df1 and df2 on 'product_id'
merged_df = pd.merge(df1, df2, on='product_id')

# Calculate total sales by category
total_sales_by_category = merged_df.groupby('category')['sales'].sum()

# Display the merged DataFrame and total sales by category
print("\nMerged DataFrame:")
print(merged_df)

print("\nTotal Sales by Category:")
print(total_sales_by_category)





"""

Problem: You have two DataFrames df1 and df2. Both DataFrames have the columns product_id, region, and sales. You need to:

Merge these two DataFrames on both product_id and region.
The merge should include all rows from df1 and only matching rows from df2. (This is a left join.)
Store the result in a new DataFrame.
Solution Steps:
Use merge() to merge the DataFrames on product_id and region.
Specify the how='left' parameter to perform a left join.
Use on=['product_id', 'region'] to specify the columns on which to join.
"""
import pandas as pd

# Sample data for df1
data1 = {
    'product_id': [1, 2, 3, 4],
    'region': ['North', 'South', 'East', 'West'],
    'sales': [100, 200, 300, 400]
}

df1 = pd.DataFrame(data1)

# Sample data for df2 (with some missing regions)
data2 = {
    'product_id': [1, 2, 3],
    'region': ['North', 'South', 'East'],
    'sales': [150, 250, 350]
}

df2 = pd.DataFrame(data2)

# Display the DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Merge df1 and df2 on product_id and region using a left join
merged_df = pd.merge(df1, df2, on=['product_id', 'region'], how='left', suffixes=('_df1', '_df2'))

# Display the merged DataFrame
print("\nMerged DataFrame:")
print(merged_df)
