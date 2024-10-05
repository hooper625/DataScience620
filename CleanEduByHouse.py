import pandas as pd
import numpy as np
cvs_file = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/Education%20By%20Household/ACSDT1Y2022.B17018-Data.csv'
cvs_file_2022 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/Education%20By%20Household/ACSDT1Y2022.B17018-Data.csv'
csv_file_5year = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/Education%20By%20Household/ACSDT5Y2022.B17018-Data.csv'
# Read the CSV file into a DataFrame
df_2023 = pd.read_csv(cvs_file)
df_2022 = pd.read_csv(cvs_file_2022)
df_5y = pd.read_csv(csv_file_5year)

#replace all null values
df_2023.replace({'-': np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)
df_2022.replace({'-': np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)
df_5y.replace({'-': np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)

#set indexing by name and geo_id
df_2023.set_index(['GEO_ID', "NAME"], inplace=True)
df_2022.set_index(['GEO_ID', "NAME"], inplace=True)
df_5y.set_index(['GEO_ID', "NAME"], inplace=True)

#merge all rows from 5year that are not in 2023
df_merge = df_2023.combine_first(df_2022)
df_merge= df_merge.combine_first(df_5y)

#turn back column name
df_merge.reset_index(inplace=True)

df_merge.to_csv('CleanEduByHouseData.csv', index=False)
