import numpy as np
import matplotlib.pyplot as plt

data = {
    'a':np.arange(50),
    'c':np.random.randint(0,50,50),
    'd':np.random.randn(50)
}

data['b'] = data['a'] + 10*np.random.randn(50)
data['d'] = np.abs(data['d'])*100
#第一個參數是x軸的輸入陣列，第二個參數是y軸的輸入陣列
#c參數是設定標記顏色，s參數設定標記大小
#data參數是輸入資料
plt.scatter('a','b',c='c',s='d',data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()