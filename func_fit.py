# 用于找出每张图的2或4个零点
# -*- coding: utf-8 -*-
import xlrd
import numpy as np
import csv

def find_4_point(array):
    zero_flag = True
    result = []
    i = 1
    for x in array:
        if zero_flag :
            if x != 0:
                result.append(i-0.5)
                zero_flag = not zero_flag
        else:
            if x == 0:
                result.append(i+0.5)
                zero_flag = not zero_flag
        i+=1
    return result

data = []
col = 180

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

for i in np.arange(0,col):
    data.append(find_4_point(sheet2.col_values(i)))

# 从列表写入csv文件
csvFile2 = open('reference/four_point.csv','w', newline='') # 设置newline，否则两行之间会空一行
writer = csv.writer(csvFile2)

for i in range(col):
    writer.writerow(data[i])
csvFile2.close()

