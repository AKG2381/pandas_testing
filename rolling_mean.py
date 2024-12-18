import pandas as pd
import numpy as np

# Generate sample data
data = {
    'A': np.random.randint(10, 100, size=100),   # Random integers between 10 and 100
    'B': np.random.randint(20, 100, size=100),   # Random integers between 20 and 100
    'C': np.random.choice(['X', 'Y', 'Z'], size=100)  # Random categories
}

df = pd.DataFrame(data)

# Display the first few rows
print(df.head())

# Filter the rows where column B > 50
df_filtered = df[df['B'] > 50].copy()
print(df_filtered.head())

# Calculate the rolling mean of A with a window size of 3 for the filtered rows
df_filtered['A_rolling_mean'] = df_filtered['A'].rolling(window=3).mean()

# Initialize the A_rolling_mean column in the original dataframe with NaN
df['A_rolling_mean'] = np.nan

# Merge the rolling mean back to the original dataframe
df['A_rolling_mean'] = df['A_rolling_mean'].combine_first(df_filtered['A_rolling_mean'])

# Display the result
print(df.head())
