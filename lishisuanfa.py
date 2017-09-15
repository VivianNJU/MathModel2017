import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

np.seterr(invalid='ignore')

def ovel_circle(x,y):

    ovel = x * x / 225 + y*y/ 1600
    if ovel <= 1:
        return 1

    # circle = (x-45)** 2 + y**2
    # if circle <= 16:
    #     return 1

    return 0


# radon变化
def radon(alpha,s):
    result,err = integrate.quad(lambda x:ovel_circle(x*np.sin(alpha)+s*np.cos(alpha),-x*np.cos(alpha)+s*np.sin(alpha)), float('-inf'),float('inf'))
    return result

n = 30
fig = plt.figure(1)
ax = fig.add_subplot(1, 1,1 ,projection='3d')  # 指定三维空间做图

y,x=np.mgrid[-100:100:30j,0:np.pi:30j]
z=[[radon(x[i][j],y[i][j]) for j in range(n)] for i in range(n)]
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
plt.show()


# xxx = []
# yyy = []
#
# for i in np.arange(-20,50):
#     for j in np.arange(-50, 50):
#         if ovel_circle(i,j,False)==1:
#             xxx.append(i)
#             yyy.append(j)
#
# plt.scatter(xxx,yyy)
# plt.show()


