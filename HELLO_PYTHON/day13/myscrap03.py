import requests

from bs4 import BeautifulSoup

url = "http://vip.mk.co.kr/newSt/rate/item_all.php"
req = requests.get(url)
req.encoding = 'euc-kr'

soup = BeautifulSoup(req.text, 'html.parser')
samsung = soup.select_one("table:nth-child(1)>tr>td>a[title='005930']").parent.parent
sdi = soup.select_one("table:nth-child(1)>tr>td>a[title='006400']").parent.parent

sam1 =samsung.select_one("td:nth-child(1)").text
sam2 =samsung.select_one("td:nth-child(2)").text
sdiChild1 =sdi.select_one("td:nth-child(1)").text
sdiChild2 =sdi.select_one("td:nth-child(2)").text

print(sam1,sam2)
print(sdiChild1,sdiChild2)

print(samsung.text)
print(sdi.text)
        

