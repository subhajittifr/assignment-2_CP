import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#dz/dt=f(t,y,z)
def f(t,y,z):
    return ((2*t*z-2*y+t**3*np.log(t))/t**2)
#dy/dt=g(t,y,z)
def g(t,y,z):
    return (z)

h=0.001
a=1
b=2
N=b-a
z_initial=0
y_initial=1
n=int(N/h)
#print(n)
t=np.linspace(a,b,n+1)
#print(x)
z=[]
y=[]
z.append(z_initial)
y.append(y_initial)

for i in range(n):
    ze=z[i]+f(t[i],y[i],z[i])*h
    z.append(ze)
    ye=y[i]+g(t[i],y[i],z[i])*h
    y.append(ye)
    
    y_actual=7*t/4+(t**3/2)*np.log(t)-0.75*t**3  #Analytical solution
plt.plot(t,y,'tab:orange',t,y_actual,'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Euler method','Analytical'])
#plt.text(1.2, 0.4, r"$y''=\frac{1}{2}-\frac{y'^2}{2}-y \ \frac{\sin(x)}{2}$", fontsize=16)
plt.text(1.2,0.4, r"$y''=\frac{\ln (t)}{t}+\frac{2}{t} \ y'-2 \ \frac{y}{t^2}$", fontsize=16)
plt.show()
#     