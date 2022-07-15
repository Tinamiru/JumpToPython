import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

ds = DaoStock()

lists = ds.selects()

arrx = np.zeros(61)
arry = range(61)

arrz = []
arr_name = []
arr_price = []

for data in lists:
    arr_name.append(data['s_name'])
    
for i in range(len(arr_name)):
    arrz.append(ds.getPrice(arr_name[i]))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

for idx, arr in enumerate(arrz):
    arr_n = np.array(arr)
    ax.plot(arrx + idx, arry, arr_n/arr_n[0])

plt.show()

