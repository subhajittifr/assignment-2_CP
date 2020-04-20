import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return (1/(x**2+y**2*(1-x)**2))

h=0.001
a=0
b=1
N=b-a
w_initial=1
n=int(N/h)
#print(n)
x=np.linspace(a,b,n+1)

#rk4:
w_rk4=[]  
w_rk4.append(w_initial)

for i in range(n):
    k1=h*f(x[i],w_rk4[i])
    k2=h*f(x[i]+h/2,w_rk4[i]+k1/2.0)
    k3=h*f(x[i]+h/2.0,w_rk4[i]+k2/2.0)
    k4 = h*f(x[i]+h,w_rk4[i]+k3)
    prk4=w_rk4[i]+(k1+2*k2+2*k3+k4)/6
    w_rk4.append(prk4)
print('x(t=3.5e6)=',w_rk4[n])
t=x/(1-x)
fig1,ax1=plt.subplots()
plt.plot(t,w_rk4,'r-o')
ax1.set_xlabel(r'$t$',fontsize=16)
ax1.set_ylabel(r'$x$',fontsize=16)
ax1.text(400, 1.6, r"$\frac{dx}{dt}=\frac{1}{x^2+t^2}$", fontsize=20)
ax1.text(400,1.3,r"$x(t=3.5\times 10^6)=2.144818$",fontsize=14)




fig1,ax2=plt.subplots()
plt.plot(x,w_rk4,'c-o')
ax2.set_xlabel(r'$x$',fontsize=16)
ax2.set_ylabel(r'$y$',fontsize=16)
ax2.text(0.1, 1.6, r"$\frac{dy}{dx}=\frac{1}{x^2+y^2 \ (1-x)^2}$", fontsize=14)


plt.show()
