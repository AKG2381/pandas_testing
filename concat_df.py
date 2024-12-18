"""
Problem: You have two DataFrames df1 and df2 with the same columns, and you need to concatenate them 
vertically (stack them on top of each other) to create a single DataFrame. Ensure that the index is reset after the concatenation.

Solution Steps:
Use pd.concat() to concatenate the DataFrames vertically.
Use reset_index() to reset the index of the resulting DataFrame.
"""

import pandas as pd

# Sample data for df1
data1 = {
    'date': pd.date_range('2023-01-01', periods=3, freq='D'),
    'product_id': [1, 2, 3],
    'sales': [100, 200, 300]
}

df1 = pd.DataFrame(data1)

# Sample data for df2
data2 = {
    'date': pd.date_range('2023-01-04', periods=3, freq='D'),
    'product_id': [4, 5, 6],
    'sales': [400, 500, 600]
}

df2 = pd.DataFrame(data2)

# Display the DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)


# Concatenate df1 and df2 vertically
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Display the concatenated DataFrame
print("\nConcatenated DataFrame:")
print(concatenated_df)
