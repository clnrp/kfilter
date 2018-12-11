#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kfilter.kalman import *
from random import *
from numpy import *
import matplotlib.pyplot as plt

# MUV 1D
dt = 0.01

# x = v0*dt + 1/2.*a*dt**2
# v = v0 + a*dt

x=matrix([[1], [0]]) # vetor de estados
A=matrix([[1, dt], [0, 1]]) # matriz de transição de estados
B=matrix([[1/2.*dt**2], [dt]]) # matriz de entradas de controle
P=matrix([[0, 0], [0, 0]]) # matriz de covariância
H=matrix([[1, 0]]) # modelo de observação
Q=matrix([[0.1, 0], [0, 0.1]]) # covariância do ruído do processo
R=50 # covariância do ruído da observação

# condições iniciais
v0 = 5
x0 = 1
a = 4


t = array([i*dt for i in range(600)])
xt = x0+v0*t+1/2.*a*t**2 # dados do modelo sem ruido
xr = xt+array([10*uniform(-1, 1) for i in range(len(xt))]) # dados do modelo com ruído

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

plt.plot(t,xt) # dados do modelo sem ruído
plt.plot(t,xr) # dados do modelo com ruído
plt.plot(t,xk) # dados obtido pelo filtro de kalman
plt.show()
