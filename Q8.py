#Question 8: 
from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
	return np.vstack((y[1], -np.exp(-2*y[1])))

def bc1(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])
def f2(x, y):
	return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))

def bc2(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])
def f3(x, y):
	return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1) ))

def bc3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

def f4(x, y):
	return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(x))  ))

def bc4(ya, yb):
	return np.array([ya[0]-2, yb[0]-2 ])
def y_exact(x): #Exact analytical Solutions:
	return np.array([np.log(x),np.exp(np.sin(x)),np.sqrt(np.sin(x)),np.sin(x)+2])
A=[1,0,np.pi/4,0];B=[2,np.pi/2,np.pi/3,np.pi] #Initial Conditions
y_initial=[0,1,2**(-1/4),2]
for i in range(4):
	if i==0:
		f=f1;bc=bc1
	elif i==1:
		f=f2;bc=bc2
	elif i==2:
		f=f3;bc=bc3
	elif i==3:
		f=f4;bc=bc4
	x=np.linspace(A[i],B[i])
	y=y_exact(x)[i]
	y_dim = np.zeros((2, x.size))
	y_dim[0]=y_initial[i]
	sol =solve_bvp(f, bc, x, y_dim)
	plt.subplots()
	plt.plot(x,sol.sol(x)[0],'tab:orange',x,y,'c')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend(['solve_bvp','Analytical'])
	if i==0:
		plt.text(1.6, 0.2, r"$y''=-e^{-2y}$", fontsize=16)
	elif i==1:
		plt.text(0.5, 1.5, r"$y''=y'\cos x-y\ \ln y$", fontsize=16)
	elif i==2:
		plt.text(0.85, 0.86, r"$y''=-(2y'^3+y^2y')\sec(x)$", fontsize=16)
	elif i==3:
		plt.text(1.5, 2.1, r"$y''=\frac{1}{2}-\frac{y'^2}{2}-y \ \frac{\sin(x)}{2}$", fontsize=16)

plt.show()

				
																			