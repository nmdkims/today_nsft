import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

#대한민국 기상청 실시간 날씨 크롤링, 기상정보가 없는 열은 제외함.
source1 = requests.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
soup1 = BeautifulSoup(source1.content,"html.parser")

table1 = soup1.find('table',{'id':'weather_table'})
data1 = []

print("#"*30)
print("\nHello! Here's today's weather!\n")
print("#"*30)

for tr in table1.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            district = td.find('a').text
            status = tds[1].string
            temp = tds[5].text
            humidity = tds[10].text
            #status 값에서는 문자열이 공백인 것처럼 등장
            #print(status)
            #strip으로 제외를 통해 비로소 공백값을 가지게 됨
            except_null_status = status.strip('\xa0')
            #맑음, 구름조금 등의 값을 가진 지역의 기후만 추출함(자신의 지역이 포함되지 않았다고 울지말것)
            if len(except_null_status)>0:
                #print(except_null_status)
                #print("{0:<9} {1:<9} {2:<9} {3:<9}".format(district,except_null_status,temp,humidity))
                #막상 데이터를 찍어보니 공백값은 \xa0이라는 값을 가지고 있음
                data1.append([district,except_null_status,temp,humidity])
                #data1.append([except_null_status])
                #print(data1)

print(data1)

# source2 = requests.get('https://www.weather.go.kr/w/weather/forecast/short-term.do')
# soup2 = BeautifulSoup(source2.content,"html.parser")
#
# table2 = soup2.find('table',{'class':'daily'})
# data2 = []
#
# for li in table2.find_all('li'):
#     daily = list(li.find('span'))
#     print(daily)
#     data2.append([daily])