import xlrd
import matplotlib.pyplot as plt

row = 256
xxx = []
yyy = []

workbook = xlrd.open_workbook('a_problem.xls')
sheet1 = workbook.sheet_by_name('1')

i = 0
while i<row:
    j = 0
    for item in sheet1.row_values(i):
        j+=1
        if float(item) == 1:
            xxx.append(j)
            yyy.append(i+1)
    i += 1

plt.scatter(xxx,yyy)
plt.show()




