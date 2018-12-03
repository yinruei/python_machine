#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:11:21 2017

@author: justinwu
"""
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.randn(6, 4),
    index=list('abcdef'),columns=list('ABCD'))
print(df1)

print(df1.loc[lambda df: df.A > 0, :])

print(df1.loc[:, lambda df: ['A', 'B']])

print(df1.iloc[:, lambda df: [0, 1]])

print(df1[lambda df: df.columns[0]])