import pandas as pd

# Specify the path to your Excel file
excel_file = 'sample.xlsx'

# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel(excel_file)

# Print the contents of the DataFrame
print(df)