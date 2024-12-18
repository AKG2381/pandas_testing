"""
Problem: You have a DataFrame df with columns product_id, year, sales, and category. 
You need to pivot the DataFrame to create a summary table where each row represents 
a product_id, and the columns represent the sales for each year and category combination.
The sales values should be aggregated (summed) for each combination.
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'year': [2021, 2021, 2022, 2021, 2022, 2021, 2022, 2022, 2021, 2022],
    'sales': [100, 150, 200, 300, 350, 400, 450, 500, 600, 650],
    'category': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)


pivoted_df = df.pivot_table(index='product_id', columns=['year','category'], values='sales', aggfunc='sum').reset_index()

print(pivoted_df)

"""
Problem: You have a DataFrame df with columns date, category, and sales. The date column contains daily dates, and you need to:

Pivot the DataFrame so that each row represents a date and each column represents a category.
The values in the pivoted DataFrame should be the sales for each category on that date.
Solution Steps:
Use pivot() to reshape the data, setting date as the index and category as the columns.
Apply the sales values as the values in the pivoted DataFrame.
"""

# Sample data
data = {
    'date': pd.date_range('2023-01-01', periods=6, freq='D'),
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'sales': [100, 200, 150, 250, 175, 300]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
# Pivot the DataFrame to have 'date' as index, 'category' as columns, and 'sales' as values
pivoted_df = df.pivot(index='date', columns='category', values='sales')

# Display the pivoted DataFrame
print("\nPivoted DataFrame:")
print(pivoted_df)
