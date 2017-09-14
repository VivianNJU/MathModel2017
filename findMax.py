# 用来找出附表2中，最对称的列,和该列的峰值
import xlrd
import numpy as np

col2 = 180
row2 = 512


def find_max(array):
    i = 0
    max_value = 0
    max_index = 0

    for item in array:
        if item > max_value:
            max_value = item
            max_index = i

        i += 1
    return max_index


# ***************************************************
def get_err(array):
    result = 0
    max_index = find_max(array)

    if max_index > (row2/2):
        for i in np.arange(1,row2-max_index):
            result+=abs(array[max_index+i]-array[max_index-i])
        result += sum(array[:(2*max_index-row2 )])

    else:
        for i in np.arange(1,max_index):
            result+=abs(array[max_index+i]-array[max_index-i])
        result += sum(array[2*max_index:])

    return result


# ***************************************************
def find_min(array):
    i = 0
    min_value = 500
    min_index = 0

    for item in array:
        if item < min_value:
            min_value = item
            min_index = i

        i += 1
    return min_index

# *****************************************************
xxx = []

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

for i in np.arange(0, col2):
    xxx.append(get_err(sheet2.col_values(i)))

min_col = find_min(xxx)+1
max_row = find_max(sheet2.col_values(min_col-1))+1

print("最对称的列："+str(min_col))
print("峰值（行）："+str(max_row))


