#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kfilter.kalman import *
from random import *
from numpy import *
import matplotlib.pyplot as plt

# MUV 1D
dt = 0.01

x=matrix([[1], [0]])
A=matrix([[1, dt], [0, 1]])
B=matrix([[1/2.*dt**2], [dt]])
P=matrix([[0, 0], [0, 0]])
H=matrix([[1, 0]])
Q=matrix([[0.1, 0], [0, 0.1]])
R=50

t = array([i*dt for i in range(600)])
v0 = 5
x0 = 1
a = 4
xt = x0+v0*t+1/2.*a*t**2
xr = xt+array([10*uniform(-1, 1) for i in range(len(xt))])

x0=matrix([[xr[0]], [v0]])

k = Kalman(A,x0,B,H,Q,R,P)
xk=[]
cnt=0
for value in xr:
    cnt+=1
    if(cnt < 100):
       xk.append(k.compute(a, value).item(0))
    elif(cnt >= 100 and cnt < 400): # região de previsão
       xk.append(k.compute(a, xk[cnt-2]).item(0))
    else :
       xk.append(k.compute(a, value).item(0))

plt.plot(t,xt)
plt.plot(t,xr)
plt.plot(t,xk)
plt.show()
