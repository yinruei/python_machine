'''
題目：企業發放的獎金根據利潤提成。利潤(I)低於或等於10萬元時，
獎金可提10%；利潤高於10萬元，低於20萬元時，低於10萬元的部分按10%提成，
高於10萬元的部分，可提成7.5%；20萬到40萬之間時，高於20萬元的部分，
可提成5%；40萬到60萬之間時高於40萬元的部分，可提成3% ；60萬到100萬之間時，高於60萬元的部分，可提成1.5%，
高於100萬元時，超過100萬元的部分按1%提成，從鍵盤輸入當月利潤I，求應發放獎金總數？

程序分析：請利用數軸來分界，定位。注意定義時需把獎金定義成長整型。
'''
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)

# 此題不懂!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!