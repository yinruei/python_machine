import numpy as np
from scipy import linalg as la

A = np.array([[1,5,2],[2,4,1],[3,6,2]])
lna,v = la.eig(A)

l1,l2,l3 = lna
print(l1,l2,l3)#特徵值(eigenvalue)

print(v)#特徵向量(Eigenvector)
print("-----------------------------------------")

print(v[:,0])
print(v[:,1])
print(v[:,2])
print("-----------------------------------------")

v1 = np.array(v[:,0]).T#將第0個eigenvector轉置
print(v1)
print("-----------------------------------------")

print(la.norm(A.dot(v1)-l1*v1))#
