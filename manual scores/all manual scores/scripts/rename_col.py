import pandas as pd
import os
import glob

# Folder containing CSV files
path = r'' 

# Loop through all CSV files in the folder
for file in glob.glob(os.path.join(path, "*.csv")):
    try:
        # Read CSV
        df = pd.read_csv(file)
        
        # Check if the dataframe has at least 5 columns
        if df.shape[1] > 4:
            # Rename column at index 4 (5th column)
            df.rename(columns={df.columns[4]: "Type"}, inplace=True)
            
            # Save back to CSV (overwrite original)
            df.to_csv(file, index=False)
            print(f"Updated: {file}")
        else:
            print(f"Skipped (not enough columns): {file}")
    
    except Exception as e:
        print(f"Error processing {file}: {e}")
