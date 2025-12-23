#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:58:08 2024
#Remove data about frames with no cotton bud from the DLC output to use in SimBA
#Adapt ilocs to your set-up
#On these filtered files - use remove cages script to remove all cage DLC output not needed for SimBA
@author: sboyanova
"""
import os

import pandas as pd

# File path to the original CSV file
directory = ''  # Change this to the directory containing your CSVs
output_directory = 'filtered_cb_DLCcsv'  # Change accordingly - new folder to save the filtered videos
os.makedirs(output_directory, exist_ok=True)  
# Loop over all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)

# Read the CSV file starting from row 3 (index 2), so row 0, 1, 2 are ignored
        df = pd.read_csv(file_path)
# Preserve the first three rows (index 0, 1, and 2)
        preserved_rows = df.iloc[:2]

# Column 33 is the 34th column, which corresponds to index 32 in zero-indexed data
# Convert the 33rd column to numeric, coercing errors to NaN
        df.iloc[2:, 33] = pd.to_numeric(df.iloc[2:, 33])

# Filter rows where the value in column 33 (index 32) is 0.8 or higher
        filtered_df = df.iloc[2:][df.iloc[2:, 33] >= 0.8]
        
        # Renumber column 0 starting from index 0 for the filtered rows
        filtered_df.iloc[:, 0] = range(len(filtered_df))
        
        # Concatenate preserved rows (first three) with the filtered rows
        output_df = pd.concat([preserved_rows, filtered_df])

# Generate a proper output file path
        output_csv = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_filtered_output.csv")

        # Write the filtered data to a new CSV file
        output_df.to_csv(output_csv, index=False)

        print(f"Filtered data has been saved to {output_csv}")
