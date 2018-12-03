import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = np.array([5,6,7])
xx, yy = np.meshgrid(x, y)
print(xx)
print(yy)
plt.plot(xx, yy, marker='.', color='k',linestyle='none')
plt.show()