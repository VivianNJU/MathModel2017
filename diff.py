import numpy as np
from scipy.optimize import leastsq

def r(theta):
    return 1

def func(p,x):
    k,b=p
    return k*x+b


def error(p, x, y):
    return func(p, x) - y  # x、y都是列表，故返回值也是个列表

def min2_mult(theta_array):
    Xi = [float(1/np.tan(t)) for t in theta_array]
    Yi = [float(r(t)/np.sin(t)) for t in theta_array]
    p0 = [1, 1]
    para = leastsq(error,p0,args=(Xi,Yi)) #把error函数中除了p以外的参数打包到args中
    x, y = para[0]
    print("x="+ str(x)+'\n'+"y="+str(y))

min2_mult(np.linspace(0,np.pi,180))





