"""
Problem: You have a DataFrame df with the following columns: product_id, sales, and category. 
The sales column contains some missing values (NaN). You need to:

Fill the missing values in the sales column with the mean value of that column.
Then, calculate the total sales for each category after filling the missing values.
Solution Steps:
Use fillna() to fill missing values in the sales column with the mean.
Use groupby() to calculate the total sales by category.
"""

import pandas as pd
import numpy as np

# Sample data with NaN in the 'sales' column
data = {
    'product_id': [1, 2, 3, 4, 5],
    'sales': [100, np.nan, 300, np.nan, 500],
    'category': ['A', 'B', 'A', 'B', 'A']
}

df = pd.DataFrame(data)

# Display the DataFrame with missing values
print(df)

# Fill missing values in 'sales' with the mean of the column
mean_sales = df['sales'].mean()
df['sales'].fillna(mean_sales, inplace=True)

# Calculate the total sales by category after filling missing values
total_sales_by_category = df.groupby('category')['sales'].sum()

# Display the total sales by category
print("\nTotal Sales by Category:")
print(total_sales_by_category)


"""
Problem: You have a DataFrame df with the columns product_id, sales, and category. 
Some rows contain duplicates, meaning the same product_id and category combination appears multiple times. You need to:

Remove the duplicate rows, keeping only the first occurrence.
After removing duplicates, calculate the total sales per category.
Solution Steps:
Use drop_duplicates() to remove duplicates based on product_id and category.
Use groupby() to calculate the total sales for each category after removing duplicates.
"""

import pandas as pd

# Sample data with duplicates
data = {
    'product_id': [1, 1, 2, 3, 3, 3, 4],
    'sales': [100, 100, 200, 300, 300, 300, 400],
    'category': ['A', 'A', 'B', 'A', 'A', 'A', 'B']
}

df = pd.DataFrame(data)

# Display the DataFrame with duplicates
print(df)


# Remove duplicates based on 'product_id' and 'category', keeping the first occurrence
df_no_duplicates = df.drop_duplicates(subset=['product_id', 'category'], keep='first')

# Calculate the total sales by category after removing duplicates
total_sales_by_category = df_no_duplicates.groupby('category')['sales'].sum()

# Display the cleaned DataFrame and the total sales by category
print("\nCleaned DataFrame (No Duplicates):")
print(df_no_duplicates)

print("\nTotal Sales by Category (After Removing Duplicates):")
print(total_sales_by_category)

