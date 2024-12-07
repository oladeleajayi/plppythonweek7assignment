# Key Operations in pandas:

# Creating DataFrames: You can create a DataFrame by loading data from various formats like CSV, Excel, or SQL databases. 
# For example:

import pandas as pd

   # Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)

# Reading Data: pandas allows you to load data from multiple sources, such as:
# Read data from a CSV file
# df = pd.read_csv('data.csv')

# Manipulating DataFrames:

# Selecting Columns: You can select a specific column like this:
# df['Age']  # Selects the Age column