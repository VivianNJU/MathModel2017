# 用于傅里叶变换的函数
import numpy as np
import math
import xlrd
import csv
import matplotlib.pyplot as plt

h = 0.2753
x_aver = 70.47

workbook = xlrd.open_workbook('A题附件.xls')
sheet2 = workbook.sheet_by_name('附件2')
g = [] # 180行，每一行512个数
for i in np.arange(0,180):
    g.append(sheet2.col_values(i))


# 求出傅里叶变换的实部
def fourier_real(omiga,k):
    k -= 1
    return h*sum(g[k][i-1]*math.cos(omiga*(i*h-x_aver)) for i in range(1,513))


# 求出傅里叶变换的实部
def fourier_im(omiga,k):
    k -= 1
    return h*sum(g[k][i-1]*math.sin(omiga*(i*h-x_aver)) for i in range(1,513))


# 傅里叶变换核心函数
def infourier(r,fai):
    step = 10
    omigas = np.arange(-500,500,step)
    result = 0

    for k in np.arange(1, 151):
        for omiga in omigas:
            alpha = omiga * r * math.cos(fai - ((k + 29) * math.pi / 180))
            result += (fourier_real(omiga, k) * math.cos(alpha) + fourier_im(omiga, k) * math.sin(alpha)) * abs(omiga)

    for k in np.arange(152, 181):
        for omiga in omigas:
            alpha = omiga * r * math.cos(fai - ((k - 151) * math.pi / 180))
            result += (fourier_real(omiga, k) * math.cos(alpha) + fourier_im(omiga, k) * math.sin(alpha)) * abs(omiga)
    result *= 1/720/math.pi*step
    return result

# 以下代码绘制“求实部函数”或“求虚部函数”图像
x = np.arange(1,5,0.01)
y = []
for omiga in x:
    y.append(fourier_real(omiga,80))

csvFile = open('data/10000.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(csvFile)

writer.writerow(x)
writer.writerow(y)
csvFile.close()

plt.plot(x, y)
plt.show()






