# 用于看出每一列的大丘对称轴变化趋势，横轴为列号，纵轴为该列对称轴
import xlrd
import numpy as np
import matplotlib.pyplot as plt

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


def find_sym(array):
    result = 0
    i = 1
    is_zero = True
    for x in array:
        if is_zero != (x == 0):
            result+=i
            is_zero = not is_zero
        i+=1

    result = int(result/2)

    if array[result]<array[result-1]:
        result -= 1

    return result


xxx = []

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

for i in np.arange(0, 25):
    xxx.append(1+find_max(sheet2.col_values(i),False))

for i in np.arange(25, 100):
    xxx.append(1+find_sym(sheet2.col_values(i)))

for i in np.arange(100, col2):
    xxx.append(1+find_max(sheet2.col_values(i),False))

# fo = open("data/对称轴们.txt", "w")
# fo.write(str(xxx))

# plt.scatter(np.arange(1,col2+1),xxx)
# plt.savefig('img/symmetry.png')
# plt.show()


