import xlrd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

x,y = np.mgrid[1:80:80j, 1:512:512j]
z = []
for i in np.arange(0,180):
    z.append(sheet2.col_values(i))

fig = plt.figure(1)
ax = Axes3D(fig)
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
plt.show()
