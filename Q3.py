import numpy as np
import matplotlib.pyplot as plt
#dy/dx=z=f(x,y,z)
def f(x,y,z):
    return (z)
#dz/dx=g(x,y,z)
def g(x,y,z):
    return (x*np.exp(x)-x+2*z-y)

h=0.05
a=0
b=1
y_initial=0
z_initial=0
n=int((b-a)/h)

x=np.linspace(a,b,n+1)

y=[]
z=[]
y.append(y_initial)
z.append(z_initial)

for i in range(n):
    k1=h*f(x[i],y[i],z[i])
    l1=h*g(x[i],y[i],z[i])
    k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
    l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
    yrk2=y[i]+k2
    zrk2=z[i]+l2
    z.append(zrk2)
    y.append(yrk2)
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$y$',fontsize=16)
plt.text(0.3,0.1,r"$y''-2y'+y=xe^x-x$",fontsize=16)
plt.plot(x,y,color = 'c',label = 'rk2')
plt.legend()
plt.grid()
plt.show()