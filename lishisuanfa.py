import numpy as np
import math
import xlrd
from scipy import integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

np.seterr(invalid='ignore')

def ovel_circle(x0, y):

    ovel = x0 * x0 / 225 + y * y / 1600
    if ovel <= 1:
        return 1

    circle = (x0 - 45) * (x0 - 45) + y * y
    if circle <= 16:
        return 1

    return 0


# radon变化
def radon(alpha,s):
    result,err = integrate.quad(
        lambda x:ovel_circle( x*np.sin(alpha)+s*np.cos(alpha), -x*np.cos(alpha)+s*np.sin(alpha)), -48, 48)
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
#
# # theta = 1*np.pi/2
# # x = np.linspace(-10,10,n)
# # y = [radon(theta,x[i]) for i in range(n)]
# # plt.scatter(x, y)
# plt.show()

# *************************************************************************


# 求radon大丘零点，theta:0~180
def find_zero(theta):
    # high = 75
    # low1 = -75
    # high1 = high
    # step = 5.0 #精度
    # step1 = step
    #
    # data = []
    # flag = True
    # while True:
    #     while step1 > 0.00001:
    #         for i in np.arange(low1, high1, step1):
    #             r = radon(theta, i)
    #             if flag != (r == 0):
    #                 low1 = i - step1
    #                 high1 = i + step1
    #                 step1 /= 10
    #                 break
    #
    #         if step1 == step:
    #             return data
    #
    #     data.append(low1)
    #     high1 = high
    #     low1 += 0.001
    #     step1 = step
    #     flag = not flag
    t2 = math.tan(theta) ** 2
    s2 = math.sqrt((225 + 1600 * t2) / (1 + t2))
    small_flag = True
    if theta>np.pi/2:
        small_flag = False
        theta = np.pi-theta
    if theta>0.741366 and theta<0.887098:
        if small_flag:
            return [-s2, 45 * math.cos(theta) + 4]
        else:
            return [-45 * math.cos(theta) - 4, s2]
    elif theta == np.pi/2:
        return [-40,40]
    else:
        return [-s2, s2]


# ****************************************************************
# theta:1~180角度，零点写入csv文件
# data = []
# for i in np.linspace(0,np.pi*179/180,180):
#     data.append(find_zero(i))
#
# csvFile2 = open('reference/radon_four_point2.csv','w', newline='') # 设置newline，否则两行之间会空一行
# writer = csv.writer(csvFile2)
#
# for i in range(180):
#     writer.writerow(data[i])
# csvFile2.close()

# *******************************************************************


def p(k, theta):
    k -= 1

    csv_reader = csv.reader(open('reference/four_point.csv', encoding='utf-8'))
    rows = [row for row in csv_reader]

    # 确定x1,x2
    x2 = float(rows[k][1])
    x1 = float(rows[k][0])
    if k > 107:
        x2 = float(rows[k][3])
        x1 = float(rows[k][2])
    del rows

    # 确定s2,s1
    s1,s2 = find_zero(theta)

    # 获取附录2所有数据，组成二位数组
    workbook = xlrd.open_workbook('a_problem.xls')
    sheet2 = workbook.sheet_by_name('2')
    sheet_data = []
    for i in np.arange(0, 180):
        sheet_data.append(sheet2.col_values(i))

    h = (s2-s1)/(x2-x1)

    radons = []
    for i in np.arange(0, x2 - x1):
        temp = radon(theta,s1+(i+0.5)*h)
        radons.append(temp)

    # radons[0] = 2.61237
    # radons[280] = 2.61387
    miu = (1/(x2-x1))*sum((sheet_data[k][int(x1+0.5+i-1)])/radons[int(i)]
                          for i in np.arange(0, x2-x1))
    return miu

    # # 用积分算法，算的很慢
    # result, err = integrate.quad(
    #     lambda x: abs(
    #         ((x-s1)/h+x1-math.floor((x-s1)/h+x1))*sheet_data[k][int(math.floor((x-s1)/h+x1))]
    #         + (math.floor((x-s1)/h+x1)+1-(x-s1)/h-x1)*sheet_data[k][int(math.floor((x-s1)/h+x1)+1)]
    #         -miu*radon(theta,x)
    #     )**2, s1,s2)


    # 用于验证理论值和实验值相差不大
    # result = []
    # for x in np.arange(1,int(x2)-int(x1)):
    #     result.append(radon(theta,s1+x*h))
    #
    # csvFile = open('reference/temp.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
    # writer = csv.writer(csvFile)
    #
    # writer.writerow(result)
    # csvFile.close()

    result = h*sum(((sheet_data[k][int(x1+0.5+i-1)])-miu*radons[int(i)])**2
        for i in np.arange(0,(x2-x1))
    )

    return [result,h,miu]


# def diff(k, theta):
#     e = 0.00001
#     dx = 0.0001
#     m = 100
#     p0 = p(k, theta)
#     p1 = p(k, theta + dx)
#     f1 = (p1 - p0) / dx
#     f2 = (p(k, theta + dx / 2) - p0) * 2 / dx
#
#     for n in np.arange(1,m+1):
#         if abs(f1-f2) < e:
#             return f2
#         f1 = f2;
#         dx /= 2
#         f2 = (p(k, theta + dx / 2) - p0) * 2 / dx
#     return False


workbook = xlrd.open_workbook('data/mygod.xlsx')
sheet2 = workbook.sheet_by_name('1')
# result = []
for i in np.arange(179, 181):
    sheet_data = list(sheet2.row_values(i - 1))
    print(p(i,sheet_data[1]))

    # temp0 = p(i,sheet_data[0])
    # temp1 = p(i, sheet_data[1])
    # temp2 = p(i, sheet_data[2])
    # if temp0[0] <= temp1[0] and temp0[0]<=temp2[0]:
    #     result.append(temp0)
    #     print("0")
    # elif temp1[0] <= temp0[0] and temp1[0] <= temp2[0]:
    #     result.append(temp1)
    #     print("1")
    # else:
    #     result.append(temp2)
    #     print("2")


    # result.append(p(i,sheet_data[1]))
    #
    # csvFile = open('reference/mygodness.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
    # writer = csv.writer(csvFile)
    #
    # writer.writerow(result)
    # csvFile.close()





















