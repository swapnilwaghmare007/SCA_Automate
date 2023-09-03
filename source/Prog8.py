import pandas as pd

# Read the Excel file
file_path = "rescored_workbook.xlsx"
df = pd.read_excel(file_path)

# Define a custom sorting order
custom_order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Not Applicable": 4}

# Add a temporary column for sorting based on custom order
df["CustomOrder"] = df.iloc[:, 4].map(custom_order)

# Sort the DataFrame based on the custom order and remove the temporary column
sorted_df = df.sort_values(by=["CustomOrder"]).drop(columns=["CustomOrder"])

# Save the sorted DataFrame back to the Excel file
sorted_file_path = "rescored_workbook.xlsx"
sorted_df.to_excel(sorted_file_path, index=False)

print("\nSorting and saving completed.\n")
print("\nAll Assessment Completed. Report Saved as 'rescored_workbook.xlsx'")
