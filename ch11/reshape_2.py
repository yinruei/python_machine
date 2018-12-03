import numpy as np

a = np.arange(10)#產生一個一維0~9的陣列
print(a)
print('--------------------------')
a = a.reshape((2,5))
print(a)
print('--------------------------')
print(np.ravel(a))#將傳回a的一維陣列