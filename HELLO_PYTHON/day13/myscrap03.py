import requests

from bs4 import BeautifulSoup

url = "http://vip.mk.co.kr/newSt/rate/item_all.php"
req = requests.get(url)
req.encoding = 'euc-kr'

soup = BeautifulSoup(req.text, 'html.parser')
trs = soup.find_all('a')

for idx, tr in enumerate(trs):
    if idx > 0:
        tds = tr.select("[title='078930']")
        print(idx, tds)

