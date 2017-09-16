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

    circle = (x-45)*(x-45)+ y*y
    if circle <= 16:
        return 1

    return 0


# radon变化
def radon(alpha,s):
    result,err = integrate.quad(lambda x:ovel_circle(x*np.sin(alpha)+s*np.cos(alpha),-x*np.cos(alpha)+s*np.sin(alpha)), -50,50)
    return result

# ********************************************************************
# 画图radon的
# n = 30
#
# fig = plt.figure(1)
# ax = Axes3D(fig)
# y,x=np.mgrid[-100:100:30j,0:np.pi:30j]
# z=[[radon(x[i][j],y[i][j]) for j in range(n)] for i in range(n)]
# ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)

# theta = 1*np.pi/2
# x = np.linspace(-10,10,n)
# y = [radon(theta,x[i]) for i in range(n)]
# plt.scatter(x, y)
# plt.show()

# *************************************************************************


# 求radon大丘零点，theta:0~180
def find_zero(theta):
    high = 75
    low1 = -75
    high1 = high
    step = 2.0 #精度
    step1 = step

    data = []
    flag = True
    while True:
        while step1 > 0.00001:
            for i in np.arange(low1, high1, step1):
                r = radon(theta, i)
                if flag != (r == 0):
                    low1 = i - step1
                    high1 = i + step1
                    step1 /= 10
                    break

            if step1 == step:
                return data

        data.append(low1)
        high1 = high
        low1 += 0.001
        step1 = step
        flag = not flag

# ****************************************************************
# theta:1~180角度，零点写入csv文件
# data = []
# for i in np.linspace(0,np.pi/2,90):
#     data.append(find_zero(i))
#
# csvFile2 = open('reference/radon_four_point.csv','w', newline='') # 设置newline，否则两行之间会空一行
# writer = csv.writer(csvFile2)
#
# for i in range(90):
#     writer.writerow(data[i])
# csvFile2.close()

# *******************************************************************




