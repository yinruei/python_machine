import pandas as pd


df = pd.read_excel("零廢棄地圖資料-副本.xlsx", sheet_name="A綠餐廳蔬食")
header = ['經度', '緯度']
data = df[header]
print(data)
a = data.to_dict()
context = {}
for key, value in a.items():
    print(key)
    for k,v in value.items():
        context.update({
            key: v
        })
        # print(k, v)
print(context)


for i in range(76):
    _dict = dict()
    _dict.update({i: i})
print(_dict)