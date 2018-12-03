#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:33:04 2017

@author: justinwu
"""

import pandas as pd

groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
       }

select_df = pd.DataFrame(dict)

print(select_df.iloc[0, 1]) # 第一列第二欄：組的人數  
print("---")  
print(select_df.iloc[0:1,:]) # 第一列：組的組名與人數  
print("---")  
print(select_df.iloc[:,1]) # 第二欄：各組的人數  
print("---")  
print(select_df["num"]) # 各組的人數  
print("---")  
print(select_df.num) # 各組的人數 