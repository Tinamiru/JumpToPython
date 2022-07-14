import requests
from bs4 import BeautifulSoup
import datetime
from day13.daostock import DaoStock
import schedule
import time

ds = DaoStock()
now = datetime.datetime.now()
ymd = now.strftime("%Y%m%d.%H%M")

url = "http://vip.mk.co.kr/newSt/rate/item_all.php"

html = requests.get(url)
html.encoding = 'EUC-KR'

soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td", "st2")

for idx, td in enumerate(tds):
    s_name = td.text
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text.replace(",", "")
    cnt = ds.insert(s_code, ymd, s_name, price)
    print(idx, "cnt : ", cnt)


def printTest():
    ymd = now.strftime("%Y%m%d.%H%M")
    print("현재시각 = " + ymd)
    
if __name__ == '__main__':

    schedule.every(1).minutes.do(printTest) #10분마다 실행

    while True:
    
        schedule.run_pending()
        time.sleep(1)
