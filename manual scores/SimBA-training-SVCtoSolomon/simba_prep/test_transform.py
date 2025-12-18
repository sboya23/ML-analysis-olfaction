import os
import pandas as pd
import numpy as np

# Folder path where the CSV files are located
folder_path = 'C:/Users/Sevda/Downloads/ML-analysis-olfaction/manual scores/SimBA-training-SVCtoSolomon/simba_prep'  # Update with your actual folder path

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # Check if the file is a CSV file
        file_path = os.path.join(folder_path, filename)

        try:
            # Read the CSV file, skipping the first 6 lines and selecting only timeON and timeOFF columns
            df = pd.read_csv(file_path, skiprows=6, usecols=['timeON', 'timeOFF'])

            # Restructure the data to fill in all the numbers in between by 0.1 increments
            all_times = []
            behaviours = []

            for on, off in zip(df['timeON'], df['timeOFF']):
                # Generate time intervals from on to off with a step of 0.1
                interval = np.arange(on, off + 0.1, 0.1).tolist()
                all_times.extend(interval)
                behaviours.extend(['sniffs_correct'] * len(interval))

            # Create a DataFrame from the times and their corresponding behaviours
            reshaped_df = pd.DataFrame({'time': all_times, 'Behaviour': behaviours})

            # Now fill in the 'doesnt_sniff' intervals between the current off and next on
            for i in range(1, len(df)):
                start = df['timeOFF'].iloc[i - 1]
                end = df['timeON'].iloc[i]
                interval = np.arange(start + 0.1, end, 0.1).tolist()
                doesnt_sniff_df = pd.DataFrame({
                    'time': interval,
                    'Behaviour': ['doesnt_sniff'] * len(interval)
                })
                reshaped_df = pd.concat([reshaped_df, doesnt_sniff_df], ignore_index=True)

            # Sort by time to ensure all times are in the correct order
            reshaped_df = reshaped_df.sort_values(by='time').reset_index(drop=True)

            # Create a new filename for the reshaped data
            new_filename = filename.replace('.csv', '_resh.1.csv')
            new_file_path = os.path.join(folder_path, new_filename)

            # Save the reshaped data back to a new CSV file
            reshaped_df.to_csv(new_file_path, index=False)

            print(f"Processed and saved: {new_file_path}")
        except Exception as e:
            print(f"Failed to process {file_path}: {e}")
