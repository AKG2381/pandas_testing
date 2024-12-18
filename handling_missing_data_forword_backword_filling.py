"""
Problem: You have a DataFrame df with columns product_id, sales, and date. Some of the sales data is missing (NaN values). 
You need to fill the missing sales values using:

Forward fill: Use the last valid value to fill the missing values.
Backward fill: Use the next valid value to fill the missing values.
You should store the results in two new columns: sales_forward_filled and sales_backward_filled.

Solution Steps:
Forward fill: Use the ffill() method to fill missing values with the previous available value.
Backward fill: Use the bfill() method to fill missing values with the next available value.
Create new columns to store the forward-filled and backward-filled values.

"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'sales': [100, np.nan, 150, 200, np.nan, 300, np.nan, 350, np.nan, 500],
    'date': pd.to_datetime([
        '2023-01-01', '2023-01-02', '2023-01-03', 
        '2023-01-01', '2023-01-02', '2023-01-01', 
        '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02'
    ])
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)



# Forward fill missing values in 'sales'
df['sales_forward_filled'] = df['sales'].ffill()

# Backward fill missing values in 'sales'
df['sales_backward_filled'] = df['sales'].bfill()

# Display the result
print(df)
