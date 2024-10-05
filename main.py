import pandas as pd
excel_file = 'dataFiles/State_Test_by_level_2023_2024.xlsx'
# Read the CSV file into a DataFrame
df = pd.read_excel(excel_file)
df.head()