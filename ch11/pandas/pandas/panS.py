#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:19:20 2017

@author: justinwu
"""

import pandas as pd

df2=pd.read_csv('MI_INDEX.csv',encoding='big5')
df =pd.DataFrame(df2)
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())
print(df.head())
print(df.index)
print(df.columns)
print(df.tail().T)