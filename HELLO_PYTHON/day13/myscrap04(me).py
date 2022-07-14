import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://vip.mk.co.kr/newSt/rate/item_all.php"

html = requests.get(url)
html.encoding = 'EUC-KR'

soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td", "st2")

for idx, td in enumerate(tds):
    s_name = td.text
    s_code = td.a['title']
    if str(s_name).__len__() < 6:
        s_name += "\t"
    price = td.parent.find_all("td")[1].text
    if str(price).__len__() < 6:
        price += "\t"
    print(idx + 1, "\t", s_name,"\t", s_code,"\t", price,"\t", datetime.today().strftime("%Y%m%d%H%M"))

