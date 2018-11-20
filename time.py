from datetime import datetime, timedelta
import time

localtime = time.localtime(time.time())
# print("本地时间为 :", localtime)

# localtime = time.asctime( time.localtime(time.time()) )
# print("本地时间为 :", localtime)
a = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
# print(a)

d1 = datetime(2005, 2, 16)
d2 = datetime(2004, 12, 31)

d = (d1-d2).days
# print(d)s
# datetime.strptime(select_time, '%Y/%m/%d %H:%M')
a = datetime.now()
b = datetime(a.year,a.month,a.day,a.hour,a.minute)
print(b)
d1 = datetime.strptime(str(b),"%Y-%m-%d %H:%M:%S")
print(d1)
d3 = d1 - timedelta(hours=12)
print(d3.ctime())
print(d3.day)
