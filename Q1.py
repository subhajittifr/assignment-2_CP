import numpy as np
import matplotlib.pyplot as plt
def f1(x,y):
    return (-9*y)
def f2(x,y):
    return (-20*(y-x)**2+2*x)
h=0.0005
a=0
b=1
N=b-a
w1_initial=np.exp(1)
w2_initial=1/3
n=int(N/h)
x=np.linspace(a,b,n+1)
#Solving the function given in part 1 of the problem:
w1=[]
w1.append(w1_initial)
for i in range(n):
    w=w1[i]/(1+9*h)
    w1.append(w)
#Solving the function given in part 2 of the problem: 
w2=[]

w2.append(w2_initial)

for i in range(n):
    w=(-1+40*h**2*(1+i)+np.sqrt(1-80*h**2*(1+i)
        +160*h**3*(1+i)+80*h*w2[i]))/(40*h) #implicit equation is quadratic which gives two roots. One of them is discarded 
                                            #since that root becomes imaginary after first iteration 
    w2.append(w)


fig1,ax1=plt.subplots()
plt.plot(x,w1,'c')
ax1.set_xlabel(r'$x$',fontsize=16)
ax1.set_ylabel(r'$y$',fontsize=16)
ax1.text(0.5, 1.5, r"$\frac{dy}{dx}=-9y$", fontsize=12)

fig2,ax2=plt.subplots()
plt.plot(x,w2,'r')
ax2.set_xlabel(r'$x$',fontsize=16)
ax2.set_ylabel(r'$y$',fontsize=16)
ax2.text(0.5, 1, r"$\frac{dy}{dx}=-20(y-x)^2+2x$", fontsize=12)
plt.show()
    