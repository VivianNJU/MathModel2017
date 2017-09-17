# 用来导出附录2每一列构成的散点图，寻找最对称的图
import xlrd
import numpy as np
import matplotlib.pyplot as plt

row1 = 256
col2 = 180

workbook = xlrd.open_workbook('A题附件.xls')
sheet2 = workbook.sheet_by_name('附件2')

i = 0
while i<col2:
    plt.scatter(np.arange(1, 513), sheet2.col_values(i))
    i += 1
    title = "img/"+str(i)+".png"
    plt.savefig(title)
    plt.close()










