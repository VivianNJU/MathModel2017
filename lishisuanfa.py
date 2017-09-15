import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

np.seterr(invalid='ignore')

def ovel_circle(x,y):

    ovel = x * x / 225 + y*y/ 1600
    if ovel <= 1:
        return 1

    circle = (x-45)** 2 + y**2
    if circle <= 16:
        return 1

    return 0


# radon变化
def radon(alpha,s):
    result,err = integrate.quad(lambda x:ovel_circle(x*np.sin(alpha)+s*np.cos(alpha),-x*np.cos(alpha)+s*np.sin(alpha)), float('-inf'),float('inf'))
    return result

# ********************************************************************
# 画图radon的
# n = 30
# fig = plt.figure(1)
# ax = Axes3D(fig)
#
# y,x=np.mgrid[-100:100:30j,0:np.pi:30j]
# z=[[radon(x[i][j],y[i][j]) for j in range(n)] for i in range(n)]
# ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
# plt.show()

# *************************************************************************


# 求radon大丘零点，theta:0~180
def find_big_zero(theta):
    low = 0
    high = 75
    step = 2.0 #精度
    while step>0.00005 :
        for i in np.arange(low,high,step):
            if radon(theta,i) == 0:
                low = i-step
                high = i
                step /= 10
                break
        if high == low:
            return 0
    return low


# # 求radon小丘零点，theta:0~180
def find_small_zero(theta):
    low = 45
    high = 75
    step = 2.0 #精度
    while step>0.00005 :
        for i in np.arange(low,high,step):
            if radon(theta,i) == 0:
                low = i-step
                high = i
                step /= 10
                break
        if high == low:
            return 0

    return low
#
data = []
for i in np.linspace(0,np.pi/2,90):
    big = find_big_zero(i)
    small = find_small_zero(i)
    if small != 45:
        data.append([-big,big,small,90-small])
    else:
        data.append(-big,big)

# 从列表写入csv文件
csvFile2 = open('reference/radon_four_point.csv','w', newline='') # 设置newline，否则两行之间会空一行
writer = csv.writer(csvFile2)

for i in range(90):
    writer.writerow(data[i])
csvFile2.close()








# 画出类似图2散点图
# xxx = []
# yyy = []
#
# for i in np.arange(-20,50):
#     for j in np.arange(-50, 50):
#         if ovel_circle(i,j,False)==1:
#             xxx.append(i)
#             yyy.append(j)
#
# plt.scatter(xxx,yyy)
# plt.show()


