


import numpy as np
import matplotlib.pyplot as plt
import math

N=[]
t=[]
a=10
b=3
dt=0.01
N.append(5.)
t.append(0)
end_time=3

for i in range(int(end_time/dt)):
        tmp=N[i]+(a*N[i]-b*(N[i])**2)*dt
        N.append(tmp)        
        t.append(dt*(i+1))
        print t[-1],N[-1]
T=np.linspace(0,3,300)
n=(10*math.e**(10*T))/(3*math.e**(10*T)-1)
plt.plot(T,n,color="red",linestyle='-',label="exact")
plt.plot(t,N,color="blue",linestyle='-',label="Eluer")
plt.xlabel("time")
plt.ylabel("pupulation")
plt.title("N-t")
plt.legend()
plt.show()
