# import urllib.request
import zipfile
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs4
import datetime
import os
import urllib.request


res ="http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-093&authorizationkey=CWB-3FB0188A-5506-41BE-B42A-3785B42C3823"
urllib.request.urlretrieve(res,"F-D0047-093.zip")
f=zipfile.ZipFile('F-D0047-093.zip')
print(f)


file = ['63_72hr_CH.xml','64_72hr_CH.xml','65_72hr_CH.xml','66_72hr_CH.xml','67_72hr_CH.xml','68_72hr_CH.xml',
        '09007_72hr_CH.xml','09020_72hr_CH.xml','10002_72hr_CH.xml','10004_72hr_CH.xml','10005_72hr_CH.xml',
        '10007_72hr_CH.xml','10008_72hr_CH.xml','10009_72hr_CH.xml','10010_72hr_CH.xml','10013_72hr_CH.xml',
        '10014_72hr_CH.xml','10015_72hr_CH.xml','10016_72hr_CH.xml','10017_72hr_CH.xml','10018_72hr_CH.xml',
        '10020_72hr_CH.xml']
CITY = []
DISTRICT = []
GEOCODE = []
DAY = []
TIME = []
T = []
TD = []
WD = []
WS = []
BF = []
AT = []
Wx = []
Wx_n = []
PoP6h = []
PoP12h = []
get_day = []
RH = []


for filename in file:
    try:
        data = f.read(filename).decode('utf8')
        # print(data)
        soup = bs4(data, "xml")
        print('soup--->', soup)
        city = soup.locationsName.text
        a = soup.find_all("location")
        for i in range(0,len(a)):
            location = a[i]
            district = location.find_all("locationName")[0].text
            print('district--->', district)
            geocode = location.geocode.text
            weather = location.find_all("weatherElement")
            # time
            time = weather[1].find_all("dataTime")
            for j in range(0,len(time)):
                x = time[j].text.split("T")
                DAY.append(x[0])
                time_1 = x[1].split("+")
                TIME.append(time_1[0])
                CITY.append(city)
                DISTRICT.append(district)
                GEOCODE.append(geocode)
                get_day.append(today)
            for t  in weather[0].find_all("value"):
                T.append(t.text)
            for td  in weather[1].find_all("value"):
                TD.append(td.text)
            for rh  in weather[2].find_all("value"):
                RH.append(rh.text)
            for wd  in weather[5].find_all("value"):
                WD.append(wd.text)
            ws = weather[6].find_all("value")
            for k  in range(0,len(ws),2):
                WS.append(ws[k].text)
                BF.append(ws[k+1].text)
            for at  in weather[8].find_all("value"):
                AT.append(at.text)
            wx = weather[9].find_all("value")
            for w in range(0,len(wx),2):
                Wx.append(wx[w].text)
                Wx_n.append(wx[w+1].text)
            rain1 = weather[3].find_all("value")
            for l in range(0,len(rain1)):
                pop6 = rain1[l].text
                PoP6h.append(pop6)
                PoP6h.append(pop6)
            rain2 = weather[4].find_all("value")
            for m in range(0,len(rain2)):
                pop12 = rain2[m].text
                PoP12h.append(pop12)
                PoP12h.append(pop12)
                PoP12h.append(pop12)
                PoP12h.append(pop12)
    except:
        break
f.close()

data = {"CITY":CITY,"DISTRICT":DISTRICT,"GEOCODE":GEOCODE,"DAY" : DAY,"TIME" : TIME,"T":T,"TD" : TD,"RH":RH,
        "WD" : WD,"WS" : WS,"BF":BF,"AT" : AT,"Wx": Wx,"Wx_n":Wx_n,"PoP6h" : PoP6h,"PoP12h" :PoP12h,"get_day":get_day}
df = pd.DataFrame(data,columns=["CITY","DISTRICT","GEOCODE","DAY","TIME","T","TD","RH","WD","WS","BF","AT","Wx","Wx_n","PoP6h","PoP12h","get_day"])
# print('df--->', df)