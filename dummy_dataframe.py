import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Age': [25, 30, 35, 28, 32, 27, 29, 31],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin', 'Sydney', 'Toronto', 'Mumbai'],
    'Salary': [50000, 60000, 75000, 55000, 68000, 52000, 58000, 72000],
    'Experience': [2, 5, 8, 3, 6, 2, 4, 7]
}

df = pd.DataFrame(data)

print("Dummy DataFrame:")
print(df.head())

print("\nDataFrame Info:")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print("hello")
