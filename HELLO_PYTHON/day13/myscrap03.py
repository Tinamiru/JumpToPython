import requests
from bs4 import BeautifulSoup

url = "http://vip.mk.co.kr/newSt/rate/item_all.php"

html = requests.get(url)
html.encoding='EUC-KR'


soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2")

for td in tds:
    s_name = td.text
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text
    print(s_name,s_code,price)  

