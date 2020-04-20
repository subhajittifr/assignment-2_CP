import numpy as np 
import matplotlib.pyplot as plt
def r(t,u1,u2,u3):
    return np.array([u1+2*u2-2*u3+np.exp(-t),u2+u3-2*np.exp(-t),u1+2*u2+np.exp(-t)])
h=0.01
a=0
b=1
u1_initial=3
u2_initial=-1
u3_initial=1
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
u1=[];u1.append(u1_initial)
u2=[];u2.append(u2_initial)
u3=[];u3.append(u3_initial)
for i in range(n):
    k1=h*r(t[i],u1[i],u2[i],u3[i])
    k2=h*r(t[i]+h/2,u1[i]+k1[0]/2,u2[i]+k1[1]/2,u3[i]+k1[2]/2)
    k3=h*r(t[i]+h/2,u1[i]+k2[0]/2,u2[i]+k2[1]/2,u3[i]+k2[2]/2)
    k4=h*r(t[i]+h,u1[i]+k3[0],u2[i]+k3[1],u3[i]+k3[2])
    u1.append(u1[i]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6)
    u2.append(u2[i]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6)
    u3.append(u3[i]+(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6)

fig, (ax1, ax2,ax3) = plt.subplots(3,figsize=(7,7))
ax1.plot(t,u1,color = 'c')
ax2.plot(t,u2,color = 'r')
ax3.plot(t,u3,color = 'm')
ax1.set_ylabel('u1')
ax2.set_ylabel('u2')
ax3.set_ylabel('u3')
plt.show()



