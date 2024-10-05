import pandas as pd
import numpy as np
Div_PatRate_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division-Participation_rates_23_24.csv'
Div_Subject_ReportGroup_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division-Subject_by_Reporting%20Group-_2023-2024.csv'
Div_PatRate_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division_Particpation_Rates_2022_2023.csv'
Sch_PatRate_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School-Participation_rates_23_24.csv'
Sch_Subject_ReportGroup_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School-Subject_by_Reporting%20Group-_2023-2024.csv'
Sch_PatRate_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School_Participation_Rates_2022_2023.csv'
Sch_TestBy_Level_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School_Test_by_level_2023_2024.csv'
State_PatRate_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State-Participation_Rates_23_24.csv'
State_SubReportGroup_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State-Subject_by_Reporting%20Group-_2023-2024%20(2).csv'
State_Part_Rates_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State_Participation_Rates_2022_2023.csv'
State_TestBy_Level_2024 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State_Test_by_level_2023_2024.csv'
Div__PassBySubj_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/division_pass_rates_by_subject_by_stu_group_2022_2023.csv'
Sch_PassBySubj_2023 = 'https://github.com/hooper625/DataScience620/blob/main/dataFiles/SOLData/school_pass_rates_by_subject_by_stu_group_2022_2023.csv'
Sch_PassByTest_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/school_pass_rates_by_test_2022_2023.csv'
State_PassBySubj_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/state_pass_rates_by_subject_by_stud_group_2022_2023.csv'
State_PassByTest_2023 = 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/state_pass_rates_by_test_2022_2023.csv'

# Read the CSV file into a DataFrame
df_2023 = pd.read_csv(cvs_file)
df_2022 = pd.read_csv(cvs_file_2022)


#replace all null values
df_2023.replace({'-': np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)
df_2022.replace({'-': np.nan, '(X)': np.nan, "N": np.nan}, inplace=True)


#set indexing by name and geo_id
df_2023.set_index(['GEO_ID', "NAME"], inplace=True)
df_2022.set_index(['GEO_ID', "NAME"], inplace=True)


#merge all rows from 5year that are not in 2023
df_merge = df_2023.combine_first(df_2022)

#turn back column name
df_merge.reset_index(inplace=True)

df_merge.to_csv('CleanPovertyData.csv', index=False)
