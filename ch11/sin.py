import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.001)#橫坐標為0到3*np.pi，每0.001選一點
y = np.sin(x)#縱座標為sin()

plt.plot(x, y)
plt.show()
