import numpy as np
import matplotlib.pyplot as plt
h=0.1
A=0
B=10
N=int((B-A)/h)
#forming a matrix:
a=np.zeros((N,N))
for i in range(1,N-1):
    a[i][i]=-2
    a[i][i-1]=1
    a[i][i+1]=1
a[0][0]=-2
a[0][1]=1
a[N-1][N-2]=1
a[N-1][N-1]=-2
#forming b matrix
b=-10*h**2*np.ones(N)

n = len(a)
x = np.zeros(n)
w=1.8
n = len(a)
x1_true=np.linalg.solve(a,b)
x_true=np.zeros(N+2)
for i in range(1,N+1):
    x_true[i]=x1_true[i-1]
#Relaxation Method:
T=np.zeros(n)
R=np.zeros(n)
n1=1000
x_arr=np.zeros((n1,n))
count=0
for i in range(n1):             
    for j in range(0, n):         
        d = b[j]                   
        for k in range(n):      
            if(j != k): 
                d-=a[j][k]*x[k] 
        x[j] = w*(d/a[j][j])+(1-w)*x[j]
        T[j]=abs(x[j]-R[j])
        R[j]=x[j]
        x_arr[i][j]=x[j]
    if(all(m <= 0.01 for m in T)):
    	break
    count+=1

X=np.zeros((count,N+2))

print(count)
for i in range(0,count):
    for j in range(1,N+1):
        X[i][j]=x_arr[i][j-1]
t=np.linspace(0,B,N+2)
for k in [10,25,50,100,150,200,300]:
    plt.plot(t,X[k],'--')
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$y$',fontsize=16)
plt.plot(t,X[count-1],color = 'c',label = 'Numerical')
plt.plot(t,x_true,color = 'black',label = 'Exact')
plt.legend()
plt.grid()
plt.show()
