# 用来导出附录2每一列构成的散点图，寻找最对称的图
import xlrd
import numpy as np
import matplotlib.pyplot as plt

row1 = 256
col2 = 180

xxx = []    # 每一行的和，一共256行
yyy = []    # 每一列的和，一共256列

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

xxx = np.arange(1, 513)

i = 0
while i<col2:
    plt.scatter(xxx, sheet2.col_values(i))
    i += 1
    title = "img/"+str(i)+".png"
    # plt.savefig(title)
    plt.close()










