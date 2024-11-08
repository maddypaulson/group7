import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = '2019_dataset_en.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Drop the columns
df = df.drop(labels=["P_SEX","P_AGE","P_PSN","P_USER","P_SAFE"],axis=1)

# Remove rows where 'P_ID' column contains 'UU' or 'NN'
df = df[~df['P_ID'].isin(['UU', 'NN'])]

# Reset the index to make the rows sequential
df.reset_index(drop=True, inplace=True)

# Sum the number of unique numbers in C_CASE column
unique_cases_count = df['C_CASE'].nunique()

# Get a specific column from the dataframe
cur_C_CASE = df['C_CASE'][0]
new_df = pd.DataFrame(columns=["C_YEAR","C_MNTH","C_WDAY","C_HOUR","C_SEV","C_CONF","C_RCFG","C_WTHR","C_RSUR","C_RALN","C_TRAF","V_ID","V_TYPE","V_YEAR","P_ISEV","C_CASE"])

gk = df.groupby(["C_CASE","V_ID"])
for name, group in gk:
    print(f"Group name: {name}")
    print(group)