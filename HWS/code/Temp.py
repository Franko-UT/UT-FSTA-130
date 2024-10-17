import pandas as pd
import numpy as np

# Create a DataFrame with some missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4]
})

# Count the number of missing values in each column
missing_values_per_column = df.isna().sum()

# Count the total number of missing values in the DataFrame
total_missing_values = df.isna().sum().sum()

# Count the number of rows with at least one missing value
rows_with_missing_values = df.isna().any(axis=1).sum()

# Count the number of missing values in each row
missing_values_per_row = df.isna().sum(axis=1)

print(missing_values_per_column)
print("Total missing values:", total_missing_values)
print("Number of rows with at least one missing value:", rows_with_missing_values)
print(missing_values_per_row)