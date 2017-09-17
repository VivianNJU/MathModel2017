import numpy as np
import math
import xlrd
import csv
import matplotlib.pyplot as plt

h = 0.2753
x_aver = 141

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')
g = [] # 180行，每一行512个数
for i in np.arange(0,180):
    g.append(sheet2.col_values(i))


def fourier_real(omiga,k):
    k -= 1
    return h*sum(g[k][i-1]*math.cos(omiga*(i*h-x_aver)) for i in range(1,513))


def fourier_im(omiga,k):
    k -= 1
    return h*sum(g[k][i-1]*math.sin(omiga*(i*h-x_aver)) for i in range(1,513))

def infourier(r,fai):
    step = 1
    omigas = np.arange(-50,51,step)

    return 1/720/math.pi*step*sum(
        sum(
            (fourier_real(omiga, k)*math.cos(2*math.pi*omiga*r*math.cos(fai-((k+29)*math.pi/180)))
            - fourier_im(omiga, k)*math.sin(2*math.pi*omiga*r*math.cos(fai-((k+29)*math.pi/180))))*abs(omiga)
            for omiga in omigas
        )
        for k in np.arange(1,181)
    )

print(infourier(3,0))

# x = np.arange(1,5,0.01)
# y = []
# for omiga in x:
#     y.append(fourier_real(omiga,80))

# csvFile = open('data/10000.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
# writer = csv.writer(csvFile)
#
# writer.writerow(x)
# writer.writerow(y)
# csvFile.close()

# plt.plot(x, y)
# plt.show()






