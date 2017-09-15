import numpy as np
import xlrd
from matplotlib.pyplot import plot, show

workbook = xlrd.open_workbook('a_problem.xls')
sheet2 = workbook.sheet_by_name('2')

x = sheet2.col_values(50)
# wave = np.cos(x)
transformed = np.fft.fft(x)  #使用fft函数对余弦波信号进行傅里叶变换。
print(transformed)  #对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
# plot(transformed)  #使用Matplotlib绘制变换后的信号。
# show()