import pandas as pd

df2 = pd.read_csv('MI_INDEX.csv', encoding='big5')
df = pd.DataFrame(df2)

print(df)
print(df.tail())#顯示後面幾列資料
print(df.shape)#顯示列數與欄數
print(df.info())#顯示DataFrame
print(df.describe())#顯示統計資訊
print(df.head())#顯示前面幾列資料
print(df.index)#索引資訊
print(df.columns)#顯示欄位
print(df.tail().T)#df.T是將陣列列轉置transpose