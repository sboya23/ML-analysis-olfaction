import os
import pandas as pd
import numpy as np

# Folder path where the CSV files are located
folder_path = 'C:/Users/Sevda/Downloads/ML-analysis-olfaction/manual scores/SimBA-training-SVCtoSolomon/simba_prep'  # Update with your actual folder path

# Iterate over all files in the folder to identify matching pairs
for filename in os.listdir(folder_path):
    if filename.endswith('_resh.1.csv'):  # Process only the _resh.1.csv files
        # Extract the first 13 characters from the filename
        base_name = filename[:13]
        
        # Look for the corresponding _info.csv file that starts with the same 13 characters
        info_filename = None
        for f in os.listdir(folder_path):
            if f.startswith(base_name) and f.endswith('_info.csv'):
                info_filename = f
                break
        
        if info_filename:
            try:
                # Construct the full paths for the files
                info_file_path = os.path.join(folder_path, info_filename)
                resh_file_path = os.path.join(folder_path, filename)
                
                # Read the length from the _info.csv file
                info_df = pd.read_csv(info_file_path)
                max_time = info_df.iloc[0, 1]  # Get the length from the second column, second row
                
                # Generate all values from 0 to max_time + 0.04 in steps of 0.04
                all_values = np.arange(0, max_time + 0.04, 0.04)
                
                # Create a full DataFrame with all values
                full_df = pd.DataFrame({'time': all_values})
                
                # Read the existing _resh.1.csv file into a DataFrame
                df = pd.read_csv(resh_file_path)

                # Initialize an empty column for the 'Behaviour'
                full_df['Behaviour'] = np.nan

                # Fill in the 'Behaviour' for the intervals
                for index, row in df.iterrows():
                    # Find the range of times in full_df that match the interval
                    matching_indices = (full_df['time'] >= row['time']) & (full_df['time'] < df['time'].shift(-1).iloc[index])
                    full_df.loc[matching_indices, 'Behaviour'] = row['Behaviour']
                
                # Fill any remaining NaN values with 'doesnt_sniff'
                full_df['Behaviour'] = full_df['Behaviour'].fillna('doesnt_sniff')
                
                # Replace '_resh.1' with '_final' in the filename
                output_file_path = os.path.join(folder_path, filename.replace('_resh.1', '_final'))
                
                # Write the updated DataFrame to a new CSV file
                full_df.to_csv(output_file_path, index=False)
                
                print(f"Processed {resh_file_path} and saved final CSV file to {output_file_path}")
                
            except Exception as e:
                print(f"Failed to process {filename} or its corresponding info file: {e}")
        else:
            print(f"No corresponding _info.csv file found for {filename}")
