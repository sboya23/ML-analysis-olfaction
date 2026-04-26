#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:15:00 2024
#On the filtered for cotton bud files - use this script to remove all cage label columns
#Adapt to ilocs to your set-up
@author: sboyanova
"""

import os
import pandas as pd

# Specify the directory containing the CSV files

directory = ''  # Change this to the directory containing your filtered CSVs
output_directory = ''  # New folder to save the processed DLC output
os.makedirs(output_directory, exist_ok=True) 
# Define the column range to keep (A to AH corresponds to columns 0 to 33 in zero-indexed)
cols_to_keep = list(range(31))  # Keeping columns up to column AE (index 30)

# Loop over all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Keep only columns up to AE
        df_filtered = df.iloc[:, cols_to_keep]
        
        # Save the modified CSV back to the file (or a new file if you want to keep the original)
        #df_filtered.to_csv(file_path, index=False)
        
      #  print(f'Processed file: {filename}')
        
        # Generate a proper output file path
        output_csv = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_filtered_output_bponly.csv")

                # Write the filtered data to a new CSV file
        df_filtered.to_csv(output_csv, index=False)

        print(f"Filtered data has been saved to {output_csv}")
