"""
Problem: You have a DataFrame df with columns product_id, sales, category, and date. You need to create a pivot table where:

The rows represent product_id.
The columns represent category.
The values represent the sum of sales.
Solution Steps:
Use pivot_table() to create the pivot table.
Set the appropriate parameters:
index for rows (product_id),
columns for columns (category),
values for the data to aggregate (sales),
and aggfunc for the aggregation function (sum).
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 1, 2, 2, 3, 3, 4, 4],
    'sales': [100, 150, 200, 250, 300, 350, 400, 450],
    'category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'date': pd.to_datetime([
        '2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', 
        '2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'
    ])
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

pivot_table = df.pivot_table(index='product_id', columns='category', values='sales', aggfunc='sum')

print(pivot_table)