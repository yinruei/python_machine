import numpy as np

nx, ny =(3,2)
#建立0到1三等份的陣列
x = np.linspace(0,1,nx)
print(x)
#建立0到1二等分的陣列
y = np.linspace(0,1,ny)
print(y)
print('-----------------')
#輸入一維矩陣x和一維矩陣y到meshgrid(x,y)
#回傳(N1,N2,N3,....Nn)維度的陣列,Ni=len(xi)
xv, yv = np.meshgrid(x,y)
print(xv)
print(yv)