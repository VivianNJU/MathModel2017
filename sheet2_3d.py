# 用于将附件2里的数据重构成一张3d图
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

workbook = xlrd.open_workbook('A题附件.xls')
sheet2 = workbook.sheet_by_name('附件2')

x,y = np.mgrid[1:180:180j, 1:512:512j]
z = []
for i in np.arange(0,180):
    z.append(sheet2.col_values(i))

fig = plt.figure(1)
ax = Axes3D(fig)
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
plt.savefig('附件2的3D图像重构.png')
plt.show()
