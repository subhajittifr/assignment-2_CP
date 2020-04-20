from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

############################################################
'''Given differential equations in the following form:
	       dy/dt=f(t,y)'''
def f1(t,y):
	return(t*np.exp(3*t)-2*y)
def f2(t,y):
	return(1-(t-y)**2)
def f3(t,y):
	return(1+y/t)
def f4(t,y):
	return(np.cos(2*t)+np.sin(3*t))

def g(t,y):
	return np.array([f1(t,y),f2(t,y),f3(t,y),f4(t,y)])
###############################################################
'''Analytical solution by Mathematica:'''
def y1(t):
	return((5*t-1)*np.exp(3*t)/25+np.exp(-2*t)/25)
def y2(t):
	return((1-3*t+t**2)/(-3+t))
def y3(t):
	return(t*(2+np.log(t)))
def y4(t):
	return(np.sin(2*t)/2-np.cos(3*t)/3+4/3)

def h(t):
	return np.array([y1(t),y2(t),y3(t),y4(t)])
#############################################################

#########################################################
A=[0,2,1,0];B=[1,3,2,1];Ya=[0,1,2,1]
#########################################################
for i in range(4):
	a=A[i]
	b=B[i]
	ya=Ya[i]
	sol=solve_ivp(lambda t,y: g(t,y)[i],[a, b], [ya],t_eval=np.linspace(a,b))
	t1=np.linspace(a,b)
	plt.plot(sol.t,sol.y[0],'b',t1,h(t1)[i],'r')
	plt.xlabel('t')
	plt.ylabel('y')
	plt.legend(['solve_ivp','Analytical'])
	if (i==0):
	    plt.text(0.4, 1.7, r"$\dot{y}=te^{3t}-2y$", fontsize=14)
	elif i==1:
	    plt.text(2.4,-20, r"$\dot{y}=1-(t-y)^2$", fontsize=16)
	elif i==2:
	    plt.text(1.2,4.5, r"$\dot{y}=1+y/t$", fontsize=16)
	elif i==3:
	    plt.text(0.6, 1.2, r"$\dot{y}=\cos2t+\sin3t$", fontsize=16)

	plt.show()