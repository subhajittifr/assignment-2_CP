import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return ((y/x)-(y/x)**2)

h=0.1
a=1
b=2
N=b-a
w_initial=1
n=int(N/h)

x=np.linspace(a,b,n+1)
w_true=x/(1+np.log(x))
w=[]
w.append(w_initial)
for i in range(n):
    pe=w[i]+f(x[i],w[i])*h
    w.append(pe)   
#Absolute Error:
abs_err=sum(w_true-w)
print('Total absolute error = ',abs_err)
#Relative Error:
rel_err=sum((w_true-w)/w_true)
print('Total Relative error = ',rel_err)

plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$y$',fontsize=16)

plt.plot(x,w,color = 'r',label = 'Euler')
plt.plot(x,w_true,color = 'c',label = 'Analytical')
plt.legend()
plt.grid()
plt.show()
    