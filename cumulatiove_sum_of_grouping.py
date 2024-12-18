"""
Problem: You have a DataFrame df with columns product_id, sales, and date. You need to calculate the 
cumulative sum of the sales for each product_id, ordered by the date. Store the result in a new column 
cumulative_sales.
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'sales': [200, 150, 300, 400, 250, 500, 600, 700, 800],
    'date': pd.to_datetime(['2023-01-01', '2023-01-03', '2023-01-05', '2023-01-02', '2023-01-04', '2023-01-06', '2023-01-01', '2023-01-02', '2023-01-03'])
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

df = df.sort_values(by=['product_id', 'date'])
df['cumulative_sales'] = df.groupby('product_id')['sales'].cumsum()
print(df)
