import numpy as np

a = np.arange(25)
print(a)
a = a.reshape((5,5))
print(a)
b = np.arange(25)
b = b.reshape((5,5))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a **2)
print(a < b)
print(a > b)
print(a.dot(b))