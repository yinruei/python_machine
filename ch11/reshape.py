import numpy as np

a = np.zeros((10,3))
print(a)
print('----------------------------------')

b = a.T
print(b)
print('----------------------------------')
c = np.reshape(b,(5,6))#產生一個5列*6行的陣列
print(c)