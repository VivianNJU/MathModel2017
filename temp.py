import lishisuanfa
import numpy as np
import math
import xlrd
import csv

def wushisuanfa():
    temp1 = []
    temp2 = []
    csv_reader = csv.reader(open('reference/four_point.csv', encoding='utf-8'))
    rows = [row for row in csv_reader]
    for k in np.arange(0,108):
        temp1.append(float(rows[k][1]))
        temp2.append(float(rows[k][0]))
    for k in np.arange(108,180):
        temp2.append(float(rows[k][3]))
        temp1.append(float(rows[k][2]))

    temp3 = []
    temp4 = []




