import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = '2019_dataset_en.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Drop the columns
df = df.drop(labels=["P_SEX","P_AGE","P_PSN","P_USER","P_SAFE","C_VEHS"],axis=1)

# Remove rows where 'P_ID' column contains 'UU' or 'NN'
df = df[~df['P_ID'].isin(['UU', 'NN'])]

# Reset the index to make the rows sequential
df.reset_index(drop=True, inplace=True)

# Print the first 20 rows of the dataframe
print(df.head(20))

# Sum the number of unique numbers in C_CASE column
unique_cases_count = df['C_CASE'].nunique()

# Get a specific column from the dataframe
cur_C_CASE = df['C_CASE'][0]



