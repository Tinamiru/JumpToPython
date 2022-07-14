import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
de = DaoStock()

sam = de.list("005930")
sk = de.list("000660")
lg = de.list("003550")

samList = [[], [], []]
skList = [[], [], []]
lgList = [[], [], []]

for idx, data in enumerate(sam):
    samList[0].insert(idx, idx)#시간
    samList[1].insert(idx, 1)#종목
    samList[2].insert(idx, data.get('price'))#금액
    
for idx, data in enumerate(sk):
    skList[0].insert(idx, idx)#시간
    skList[1].insert(idx, 2)#종목
    skList[2].insert(idx, data.get('price'))#금액
    
for idx, data in enumerate(lg):
    lgList[0].insert(idx, idx)#시간
    lgList[1].insert(idx, 3)#종목
    lgList[2].insert(idx, data.get('price'))#금액
    
# z(시간),y(종목),x(가격)
ax.plot(samList[0], samList[1], samList[2])  # 파랑 = 삼성
ax.plot(skList[0], skList[1], skList[2])  # 주황 = sk
ax.plot(lgList[0], lgList[1], lgList[2])  # 초록 = lg

plt.show()
