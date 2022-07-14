import requests
from bs4 import BeautifulSoup
from daostock import DaoStock
import datetime

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
print("현재시간 - ", ymd, "실행")

