import pandas as pd
import numpy as np
import os

# Folder where you want to save the cleaned files
output_folder = 'cleaned_SOL_files'

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List of DataFrame names and their corresponding URLs
dataframes = {
    'Div_PatRate_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division-Participation_rates_23_24.csv',
    'Div_Subject_ReportGroup_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division-Subject_by_Reporting%20Group-_2023-2024.csv',
    'Div_PatRate_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division_Particpation_Rates_2022_2023.csv',
    'Sch_PatRate_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School-Participation_rates_23_24.csv',
    'Sch_Subject_ReportGroup_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School-Subject_by_Reporting%20Group-_2023-2024.csv',
    'Sch_PatRate_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School_Participation_Rates_2022_2023.csv',
    'Sch_TestBy_Level_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School_Test_by_level_2023_2024.csv',
    'State_PatRate_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State-Participation_Rates_23_24.csv',
    'State_SubReportGroup_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/School-Subject_by_Reporting%20Group-_2023-2024.csv',
    'State_Part_Rates_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State_Participation_Rates_2022_2023.csv',
    'State_TestBy_Level_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/State_Test_by_level_2023_2024.csv',
    'Div_PassBySubj_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/division_pass_rates_by_subject_by_stu_group_2022_2023.csv',
    'Sch_PassBySubj_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/school_pass_rates_by_subject_by_stu_group_2022_2023.csv',
    'Sch_PassByTest_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/school_pass_rates_by_test_2022_2023.csv',
    'State_PassBySubj_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/state_pass_rates_by_subject_by_stud_group_2022_2023.csv',
    'State_PassByTest_2023': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/state_pass_rates_by_test_2022_2023.csv',
    'Div_ByTestLevel_2024': 'https://raw.githubusercontent.com/hooper625/DataScience620/refs/heads/main/dataFiles/SOLData/Division_Test_by_level_2023_2024%20.csv'
}

# Dictionary to store DataFrames
dfs = {}

# Load and replace values in each DataFrame
for name, url in dataframes.items():
    # Read the CSV file into a DataFrame
    df = pd.read_csv(url)
    # Store the cleaned DataFrame in the dfs dictionary
    dfs[name] = df
    # Replace '>', '<', and 'N' with NaN
    df.replace({'>': np.nan, '<': 0, 'N': np.nan}, inplace=True)
    #save to new file
    dfs[name].to_csv(os.path.join(output_folder, f'clean_{name}.csv'), index=False)



print(f"Saved cleaned data to clean_{name}.csv")
