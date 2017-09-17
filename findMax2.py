# 用于找出峰值最大的列
import xlrd
import numpy as np

col2 = 180


def find_max(array, is_value):
    i = 0
    max_value = 0
    max_index = 0

    for item in array:
        if item > max_value:
            max_value = item
            max_index = i
        i += 1

    if is_value:
        return max_value
    else:
        return max_index


xxx = []

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

for i in np.arange(0, col2):
    xxx.append(find_max(sheet2.col_values(i),True))

print("峰值最大的是第"+str(find_max(xxx,False)+1)+"列")
