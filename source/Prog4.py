
import pandas as pd

df = pd.read_excel('rescored_workbook.xlsx')

# Define a function to update the values
def update_values(row):
    if pd.isnull(row[15]):
        row[15] = 'Not Applicable'
        row[13] = 'Not Applicable'
        row[4] = 'Not Applicable'
    return row

# Apply the function to each row in the DataFrame
df = df.apply(update_values, axis=1)

df.to_excel('rescored_workbook.xlsx', index=False, engine='openpyxl')
