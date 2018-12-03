import pandas as pd

SalaryDic = {
    "John":'50000',
    "Mary":'20000',
    "Ivy":'90000',
    "Steve":'35000',
    "David":'85000'
}

myDic = pd.Series(SalaryDic, index=SalaryDic.keys())
print(myDic[0])
print(myDic['Ivy'])
print(myDic[[0,1,3]])
print(myDic[['John','Ivy','David']])
