"""
Problem: You have a DataFrame df with columns date and sales, where the date column contains timestamps in daily frequency. 
You need to resample the data to a monthly frequency, summing up the sales for each month.

Solution Steps:
Convert date column to datetime format if it’s not already in datetime.
Use resample() to change the frequency to monthly ('M'), applying the sum aggregation on sales.
"""

import pandas as pd
import numpy as np

# Sample data
data = {
    'date': pd.date_range('2023-01-01', periods=60, freq='D'),
    'sales': np.random.randint(100, 500, size=60)
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df.head())


# Resample to monthly frequency and sum the sales
df['date'] = pd.to_datetime(df['date'])  # Ensure the 'date' column is datetime
monthly_sales = df.resample('M', on='date')['sales'].sum()

# Display the resampled data
print(monthly_sales)