# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:10:14 2023

@author: Sevda
"""
# import libraries
import pandas as pd
import glob
import re


# define folder directory to look in 
path =r' '
allFiles = glob.glob(path + "/*.csv")
# make a list of all the files in the folder
list_ = []
for file_ in allFiles:
    # define sheet name and place data starts
    df = pd.read_csv(file_, index_col=None, dtype=str, usecols = ['Behavior','Total Duration(s)'])
    
    # create a variable with the filename
    df['filename']= file_
    
    
    # Extract the mouse ID **only once per file** from the filename (starting with 'APP' followed by 5 characters)
    match = re.search(r'C9ORF[^_]*|TDP43[^_]*|TDP[^_]*|C9O[^_]*', file_)
    mouse_id = match.group(0) if match else None
    
    # Extract the 7th character after "roi_20"
    odour_match = re.search(r'_000000_(.{9})', file_)
    odour_char = odour_match.group(1)[-1] if odour_match else None  # Get the 7th character

    # Assign label based on extracted character
    odour_mapping = {'F': 'Familiar', 'W': 'Water', 'N': 'Novel'}
    odour = odour_mapping.get(odour_char, None)  # Assign label
    
    # set row number as index 
    df.index = range(len(df))    
    
    ### GET Odour1.1 
    # set index selection based on text
    index_start = df[df.iloc[:,0]=='Odour1.1'].index.values.astype(int)[0]  
    # select the data between set indexes
    df_11 = df.query('index == 0')
    
    ### GET Odour1.2
    # set index selection based on text
    index_start2 = df[df.iloc[:,0]=='Odour1.2'].index.values.astype(int)[0]  
    # select the data between set indexes
    df_12 = df.query('index == 1')    
    
    ### GET Odour1.3
    # set index selection based on text
    index_start3 = df[df.iloc[:,0]=='Odour1.3'].index.values.astype(int)[0]  
    # select the data between set indexes
    df_13 = df.query('index == 2')                                                  
   
    # merge the data together
    df_all = pd.merge(df_11, df_12, left_on = ['filename'], right_on = ['filename'], how = 'left')
    df_all = pd.merge(df_all, df_13, left_on = ['filename'], right_on = ['filename'], how = 'left')
    
    # Add mouse_id and Odour only **once per file** after merging
    df_all.insert(1, 'mouse_id', mouse_id)
    df_all.insert(2, 'Odour', odour)
    
    # stack all files on top of each other
    list_.append(df_all)
log = pd.concat(list_, axis=0)

# write to csv
log.to_csv(r'\odour1_by_order.csv', index = False)