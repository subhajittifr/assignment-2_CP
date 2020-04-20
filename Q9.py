import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def f(y,t):
    return (y**2+y)/t
def rk4(w,x,h):
    k1 = h*f(w,x)
    k2 = h*f(w+k1/2,x+h/2)
    k3 = h*f(w+k2/2,x+h/2)
    k4 = h*f(w+k3,x+h)
    return  w+(k1+2*k2+2*k3+k4)/6
h=0.1
N_max=5000
x_initial=1
Y_initial=-2
w_initial=-2
x,Y,w=[],[],[]
x.append(x_initial);Y.append(Y_initial);w.append(w_initial)
del_err=1e-4
for i in range(N_max):
	W1=Y[i];W2=w[i];X=x[i]
	if(X>=3):
		break
	y1=rk4(W1,X,h)
	y2=rk4(W2,X,2*h)
	err=abs((y1-y2)/30)
	hp=h*(del_err*h/err)**(1/4)
	if(err>del_err):
		h=hp
		y1=rk4(W1,X,h)
		y2=rk4(W2,X,2*h)
		Y.append(y1)
		w=Y
	else:
		Y.append(y1)
		w=Y
	x.append(X+h)
	
Y_true=odeint(f,Y[0],x) #True solution

E=np.zeros(len(Y))
for i in range(len(Y)):
    E[i]=(Y_true[i]-Y[i])/Y_true[i]
print('The absolute accuracy of the solution is given by:',abs(sum(E)))

with plt.style.context('dark_background'):

    
    plt.plot(x,Y_true,'r-o',label = 'Actual')
    plt.plot(x,Y,'c-o',label = 'Adaptive Step Size')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()


