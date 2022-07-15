import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

ds = DaoStock()

arrx = np.zeros(61)


arry = list(range(61))

arrz = []
arr_name = ["삼성전자","LG","SK"]

arrz.append(ds.selects(arr_name[0]))
arrz.append(ds.selects(arr_name[1]))
arrz.append(ds.selects(arr_name[2]))

# for i in arrz1:
#     arrz1p.append(i/arrz1[0])
# for i in arrz2:
#     arrz2p.append(i/arrz2[0])
# for i in arrz3:
#     arrz3p.append(i/arrz3[0])


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot(arrx,arry,arrz[0])
ax.plot(arrx+1,arry,arrz[1])
ax.plot(arrx+2,arry,arrz[2])

plt.show()



