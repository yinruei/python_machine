import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.randn(6,4),
    index=list('abcdef'),columns=list('ABCD'))

print(df1)
print('-------------------------------')
df2 = df1.loc[lambda df1: df1.A > 0, :]
# print(df2)

df3 = df1.loc[:, lambda df1: ['A','B']]
print(df3)
('-------------------------------')

df4 = df1.iloc[:, lambda df1: [0, 1]]
print(df4)

df5 = df1[lambda df1:df1.columns[1]]
print(df5)