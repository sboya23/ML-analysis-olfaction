# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:10:14 2023

@author: Sevda
"""
# import libraries
import pandas as pd
import glob

# define folder directory to look in 
path = r'C:\Users\Sevda\Downloads\ml_paper\c9-tdo43-reassessment\combined\extra3\manual scores\all manual scores' 
allFiles = glob.glob(path + "/*.csv")
# make a list of all the files in the folder
list_ = []
for file_ in allFiles:
    # define sheet name and place data starts
    df = pd.read_csv(file_, index_col=None, dtype=str, usecols = ['Behavior','Total Duration(s)', 'Type'])
    
    # create a variable with the filename
    df['filename']= file_
    
    # set row number as index 
    df.index = range(len(df))
    
    ### GET SHIFT TIMES
    # set index selection based on text
    #index_start = df[df.iloc[:,0]=='Shift:'].index.values.astype(int)[0]    
    #index_finish = df[df.iloc[:,0]=='Next planned shifts:'].index.values.astype(int)[0] - 1
    # select the data between set indexes
    #df_shifts = df.query('index > @index_start & index < @index_finish')
    
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
    
    
    # stack all files on top of each other
    list_.append(df_all)
log = pd.concat(list_, axis=0)
## rename columns
#log.rename(columns={log.columns[0]: "Shift", log.columns[1]: "Start", log.columns[2]: "Finish",log.columns[3]: "Production Volume", log.columns[4]: "Notes",  log.columns[5]: "filename", log.columns[7]: "Date", log.columns[12]: "Manager on shift"  }, inplace=True)
# retain only useful columns
#log = log[['Date', 'Manager on shift', 'Shift','Start','Finish','Production Volume','Notes','filename']]
# write to csv
log.to_csv(r'C:\Users\Sevda\Downloads\ml_paper\c9-tdo43-reassessment\combined\extra3\manual scores\all manual scores\combined\odour1_by order.csv', index = False)