import numpy as np


def s(theta):
    return 0


def qiudao(theta0, e, dx, m):
    f1 = (s(theta0+dx)-s(theta0))/dx
    f2 = (s(theta0+dx/2)-s(theta0))*2/dx

    for n in np.arange(1,m+1):
        if abs(f1-f2) < e:
            return f2
        f1 = f2;
        dx /= 2
    f2 = (s(theta0 + dx / 2) - s(theta0)) * 2 / dx