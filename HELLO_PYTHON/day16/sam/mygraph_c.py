import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day16.daostocksink import DaoStock

ds = DaoStock()

lists = ds.selects()

arrx = np.zeros(894)
arry = range(894)

arr_n = []
arrz = []

for key in lists[0].keys():
    arr_n.append(key)
    
for i in range(894):
    d = []
    for j in range(894):
        d.append(lists[j][arr_n[i]])
    arrz.append(d)
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

for idx, arr in enumerate(arrz):
    result = 0;
    arr_p = np.array(arr)
    if arr_p[idx] > 0:
        result = arr_p / arr_p[0]
    print("idx-",idx,arr_p[0])
    ax.plot(arrx + idx, arry, result)
    
plt.show()
    
