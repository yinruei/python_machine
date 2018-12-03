import numpy as np
import matplotlib.pyplot as plt

#建立一個10000 normal 平均值為2,0.5^2 標準差

mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)

#畫500柱狀histogram圖
plt.hist(v, bins=500, normed=1)
plt.show()