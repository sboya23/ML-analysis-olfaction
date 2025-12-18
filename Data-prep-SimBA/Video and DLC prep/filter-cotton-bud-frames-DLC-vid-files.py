#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:49:39 2024
#Code to filter out frames with no cotton bud from olfaction task videos - using video files and DLC analysis output
@author: sboyanova
"""

import pandas as pd
import cv2
import os

# Define input and output folder paths
input_folder = "path"  # Folder containing the CSV and video files with matching file names
output_folder = "filtered_videos"  # Folder to save the filtered videos
os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):  # Only process video files
        video_path = os.path.join(input_folder, filename)
        
        # Generate the corresponding CSV file path (assumes CSV and video names are similar)
        csv_filename = filename.replace(".mp4", ".csv")
        csv_path = os.path.join(input_folder, csv_filename)
        
        # Check if the CSV file exists for the video
        if not os.path.exists(csv_path):
            print(f"No corresponding CSV found for {filename}. Skipping.")
            continue
        
        # Load the CSV data
        df = pd.read_csv(csv_path)

        
        # Convert the 33rd column to numeric, coercing errors to NaN #Adapt to revelant col n - filter by cotton bud probability
        df.iloc[:, 33] = pd.to_numeric(df.iloc[:, 33], errors='coerce')

        # Filter rows where the value in column 33 (index 32) is 0.8 or higher
        filtered_df = df[df.iloc[:, 33] >= 0.8]

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Check if the video opened successfully
        if not cap.isOpened():
            print(f"Error: Could not open video file {filename}.")
            continue

        # Read the first frame to get frame properties (width, height, FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Define the codec and create a VideoWriter object for the output video
        output_video = os.path.join(output_folder, f"filtered_{filename}")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' or other codecs if needed
        out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

        # Loop through the video frames and filter based on the CSV data
        frame_index = 0
        saved_frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break  # End of video

            # Check if the current frame index exists in the filtered CSV rows
            if frame_index in filtered_df.index:
                # Write the frame into the output video if it meets the condition
                out.write(frame)
                saved_frame_count += 1
            
            frame_index += 1

        # Release the video objects
        cap.release()
        out.release()

        print(f"Filtered video saved as {output_video}, containing {saved_frame_count} frames.")
