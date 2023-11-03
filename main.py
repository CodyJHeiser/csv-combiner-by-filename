import os
import pandas as pd

# Define the directory where the CSV files are located
directory = '/Users/codyheiser/Documents/DataCEVA/FlyingBull/states_unzipped'

# List to hold all the DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Extract state and internet type from the filename
        parts = filename.split('_')
        state = parts[0]
        internet_type = parts[1].replace('.csv', '')
        
        # Read the CSV file into a DataFrame
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        
        # Add the 'state' and 'internet_type' columns
        df['state'] = state
        df['internet_type'] = internet_type
        
        # Append this dataframe to the list
        dataframes.append(df)

# Concatenate all dataframes into one
combined_dataframe = pd.concat(dataframes, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_csv_path = os.path.join(directory, 'combined_data.csv')
combined_dataframe.to_csv(combined_csv_path, index=False)

print(f"Combined CSV created at {combined_csv_path}")
