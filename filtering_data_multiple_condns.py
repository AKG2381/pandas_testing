"""
Problem: You have a DataFrame df with columns product_id, sales, and date. You need to filter the rows where:

The sales value is greater than 200.
The date is in the year 2023.
After filtering, you should return a new DataFrame containing only the rows that meet both conditions.

Solution Steps:
Use Boolean conditions to filter the data for sales greater than 200 and date in 2023.
Apply the conditions together using the & (and) operator.
Use loc[] to filter and return the result.
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'product_id': [1, 2, 3, 4, 5, 6],
    'sales': [150, 300, 400, 180, 250, 350],
    'date': pd.to_datetime([
        '2023-01-01', '2023-02-15', '2023-03-10', 
        '2022-12-20', '2023-05-05', '2023-08-21'
    ])
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Filter rows where sales is greater than 200 and date is in 2023
filtered_df = df[(df['sales'] > 200) & (df['date'].dt.year == 2023)]

# Display the filtered DataFrame
print(filtered_df)