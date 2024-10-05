import pandas as pd
import numpy as np
excel_file = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/ACSDT1Y2023.B17018-Data.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(excel_file)

#Replace missing values
df.replace({'-':np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)