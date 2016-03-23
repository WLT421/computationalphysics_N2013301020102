
# -*- coding: utf-8 -*-

from pylab import *
import pickle

#本程序是用来计算具有一定初速的物体在加速度g的情况下自由落体时速度，位移随时间的变化


t_total=0
dt=0
t=[0,]
d=[0,]
v=[]
g=0
n=0
m=0
a=0

def initialize():
    global t_total,dt,v,n,g,m,a
    print 'Enter total time(s）:'
    t_total=float(raw_input())
    print 'Enter the initial velocity（m/s):'
    v=[float(raw_input()),]
    print 'Enter g(m/s**2):'
    g=float(raw_input())
    print 'Enter dt(s):'
    dt=float(raw_input())
    n=int(t_total/dt)

def calculate():
    global dt,v,n,g,t,d,m,a
    for i in range(1,n+1):
        t.append(dt*i)
        dv=(g)*dt
        d.append(d[-1]+(v[-1]+dv/2)*dt)
        v.append(v[-1]+dv)
    

def output():
    global v,t,d,n
    for i in range(0,n+1):
        print t[i],'  ',v[i],'  ',d[i]
    
initialize()
calculate()
output()

plot(t,v,'--')
plot(t,d,'-')
#scatter(t,d)
show()
savefig('output.jpg')