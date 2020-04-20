import numpy as np
import matplotlib.pyplot as plt
#dz/dx=-10=f(x,y)
def f(x,y):
    return (-10)
#dy/dx=z=g(x,z)
def g(x,z):
    return (z)

h=0.001
a=0
b=10
A=40
B=60
z_initial=np.linspace(A,B,B-A+1) ##Setting up z(0) from 40 to 60.
y_initial=0
N=b-a
n=int(N/h)
x=np.linspace(a,b,n+1)
z=np.zeros((z_initial.size,x.size))    
for i in range(len(z_initial)):
        z1=[]
        z1.append(z_initial[i])
        for j in range(n):
            ze=z1[j]+f(x[j],z1[j])*h
            z1.append(ze)
        z[i]=z1
Y=np.zeros((z_initial.size,x.size))   
for i in range(z_initial.size):
    y=[]
    y.append(y_initial)
    for j in range(n):
        ye=y[j]+g(x[j],z[i][j])*h
        y.append(ye)
    Y[i]=y
    count=0

p=[]
for i in range(z_initial.size):
    p.append(abs(Y[i][n]))
###########################Use of numpy.argmin######################
count=np.argmin(p,axis=0)

print("The value of z(0) is given by:",z[count][0])
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$y$',fontsize=16)
for k in [x for x in range(7,14) if x != count]:
    plt.plot(x,Y[k],'--')
plt.plot(x,Y[10],color = 'c',label = 'y vs x(true)')
plt.text(4, 53, r"$y''=-g$", fontsize=16)
plt.text(4, 30, r"$y'=z$", fontsize=16)
plt.text(4, 10, r"$z'=-g$", fontsize=16)
plt.text(4, -15, r"$z_{true}(0)=50$", fontsize=13)
plt.title('Shooting Method')
plt.legend()
#plt.grid()
plt.show()





    
