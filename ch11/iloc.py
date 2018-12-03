import pandas as pd

groups = ["Working", "Dancing", "cooking", 
          "Movies", "Sports", "Fishing"]

num = [12, 15, 3, 8, 29, 38]

dict = {"groups": groups,
        "num": num
        }

mydf = pd.DataFrame(dict)
# print(mydf)
print(mydf.iloc[:,:])#所有列和欄
print("------------------------")
print(mydf.iloc[0,1])#第一列和第二欄:組的人數
print("------------------------")
print(mydf.iloc[0:2,:])#第一列和第二列:組的組名與人數
print("------------------------")
print(mydf.iloc[:,0])#第一欄:各組人數
print("------------------------")
print(mydf["num"])#各組人數
print("------------------------")
print(mydf.num)#各組的人數
