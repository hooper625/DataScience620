import pandas as pd
import numpy as np
cvs_file = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/Education%20By%20Household/ACSDT1Y2023.B17018-Data.csv'
cvs_file_2022 = ''
csv_file_5year = ''
# Read the CSV file into a DataFrame
df = pd.read_csv(cvs_file)

#Replace missing values
df.replace({'-':np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)

cleaned_df = "Poverty_Status_by_Education_Household.csv"
df.to_csv(cleaned_df)

print(df.head())