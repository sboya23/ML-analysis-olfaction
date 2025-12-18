import os
import csv

# Set the folder path (you can change this)
folder_path = "path"  # path to all your files

# Output CSV filename
output_csv = "file_list.csv"

# Get list of files
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Write to CSV
with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Filename"])  # Header
    for filename in file_list:
        writer.writerow([filename])

print(f"✅ {len(file_list)} files written to {output_csv}")
