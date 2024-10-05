import os
import pandas as pd

# Path to the folder containing the .xlsx files
folder_path = './dataFiles/SOLData'


# Function to convert Excel (.xlsx) to CSV
def convert_xlsx_to_csv(xlsx_file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(xlsx_file_path)

    # Construct the CSV file path (replace .xlsx with .csv)
    csv_file_path = xlsx_file_path.replace('.xlsx', '.csv')

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"Converted {xlsx_file_path} to {csv_file_path}")


# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):  # Process only .xlsx files
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Convert the file from .xlsx to .csv
        convert_xlsx_to_csv(file_path)

print("All .xlsx files have been converted to .csv.")
