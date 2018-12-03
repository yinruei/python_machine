import matplotlib.pyplot as plt

month1 = [1,2,3,4,5,6,10,12]
month2 = [1,3,4,5,6,7,11,12]

sale1 = [20000,40000,60000,80000,100000,120000,140000,160000]
sale2 = [10000,20000,30000,15000,120000,80000,60000,210000]

plt.plot(month1, sale1, lw=2, label='Ivy Lin')#lw為線寬
plt.plot(month2, sale2, lw=2, label='Jonny Wu')
plt.xlabel('month')
plt.ylabel('dollars')
plt.legend()
plt.title('matplotlib example')
plt.show()