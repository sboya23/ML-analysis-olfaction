# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 12:58:33 2025

@author: Sevda
"""

import pandas as pd
import glob


path =r''
allFiles = glob.glob(path + "/*.csv")

dfs = list()

for filename in allFiles:
    data = pd.read_csv(filename)
    dfs.append(data)
    
df_combined = pd.concat(dfs, ignore_index=True)

df_combined.to_csv("all.csv", index = False)