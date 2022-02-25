import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

source = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(source.content, "html.parser")

table = soup.find('table', {'class': 'table_develop3'})
data = []

print("#" * 30)
print("\nHello! Here's today's weather!\n")
print("#" * 30)

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temp = tds[5].text
            humidity = tds[9].text
            print("{0:<7} {1:<7} {2:<7}".format(point, temp, humidity))
            data.append([point, temp, humidity])

print("#" * 30)
print("\nIt ends here. thanks!\n")
print("#" * 30)

print(data)

with open('weather.csv', 'w') as f:
    f.write('지역, 온도, 습도\n')
    for i in data:
        f.write('{0},{1},{2}\n'.format(i[0], i[1], i[2]))

df = pandas.read_csv('weather.csv', index_col='지역', encoding='euc-kr')

city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]

font_name = mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\malgun.ttf').get_name()
mpl.rc('font', family=font_name)

ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=15)
ax.set_xlabel('도시', fontsize=15)
ax.set_ylabel('기온/습도', fontsize=15)
ax.legend(['기온', '습도'], fontsize=15)

plt.show()