import numpy as np
import pandas as pd

df2 = pd.read_csv('C:\\Users\\yinruei\\Desktop\\python機器學習\\python_machine\\ch11\\pandas\\pandas\\data\\201711_F3_1_8_2330.csv',engine='python', 
                  encoding='big5', error_bad_lines=False,header=None,names=["日期","成交股數","成交金額","開盤價",
                  "最高價","最低價","收盤價","漲跌價差","成交筆數"])
print(df2)
print('-------------------------------')
df = pd.DataFrame(df2)
print(df.iloc[:,5])

print(df.shape)
print(df.info())