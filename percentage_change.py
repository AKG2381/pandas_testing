"""
Problem: You have a DataFrame df with columns product_id, sales, and date. You need to calculate the 
percentage change in sales for each product_id from one date to the next, and store the result in a 
new column named sales_percentage_change.

Solution Steps:
Sort the DataFrame by product_id and date to ensure the correct order of records.
Use the pct_change() function to calculate the percentage change in sales for each product_id.
Create a new column called sales_percentage_change to store the calculated percentage change.
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    'sales': [100, 150, 200, 300, 350, 400, 500, 550, 600, 1000, 1100],
    'date': pd.to_datetime([
        '2023-01-01', '2023-01-02', '2023-01-03', 
        '2023-01-01', '2023-01-02', '2023-01-03', 
        '2023-01-01', '2023-01-02', '2023-01-03', 
        '2023-01-01', '2023-01-02'
    ])
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Sort the DataFrame by product_id and date to calculate the change in correct order
df = df.sort_values(by=['product_id', 'date'])

# Calculate the percentage change in sales for each product_id
df['sales_percentage_change'] = df.groupby('product_id')['sales'].pct_change() * 100

# Display the result
print(df)
