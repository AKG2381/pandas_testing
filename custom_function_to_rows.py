"""
Problem: You have a DataFrame df with columns product_id, sales, and category. You need to create a new column 
sales_category that combines the sales and category columns based on certain conditions:

If sales is greater than 300, categorize as "High Sales".
If sales is between 100 and 300 (inclusive), categorize as "Medium Sales".
If sales is less than 100, categorize as "Low Sales".
You need to apply a custom function row by row to create the sales_category column.

Solution Steps:
Define a custom function that takes a row and returns the appropriate category based on the sales value.
Use apply() with the custom function to apply it row-wise to create the sales_category column.
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'sales': [100, 150, 250, 300, 350, 500, 550, 600, 50, 200],
    'category': ['A', 'B', 'C', 'A', 'B', 'A', 'B', 'C', 'A', 'B']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Define a custom function that takes a row and returns the appropriate category based on the sales value.
def categorize_sales(row):
    sales = row['sales']
    if sales > 300:
        return 'High Sales'
    elif 100 <= sales <= 300:
        return 'Medium Sales'
    else:
        return 'Low Sales'

# Use apply() with the custom function to apply it row-wise to create the sales_category column.
df['sales_category'] = df.apply(categorize_sales, axis=1)
print(df)