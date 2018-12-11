#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kfilter.simplify import *
from sympy import *

dt = Symbol('dt')
angle,bias = symbols('angle, bias')
Q00,Q11 = symbols('Q_angle, Q_bias')

# angle = angle0 + (newVelocity - bias)*dt
# bias  = bias

x = Matrix([[angle], [bias]]) # vetor de estados
A = Matrix([[1, -dt], [0, 1]]) # matriz de transição de estados
B = Matrix([[dt], [0]]) # matriz de entradas de controle
u,z = symbols('newVelocity,newAngle')
H = Matrix([[1, 0]]) # modelo de observação
Q = Matrix([[Q00, 0], [0, Q11]])*dt # covariância do ruído do processo

# imprimir dados
print(x)
print(A)
print(B)
print(u)
print(H)

simplify = Simplify(A,x,B,u,z,H)
simplify.setQ(Q)
simplify.compute() # calcular simplificações
simplify.printq() # imprimir filtro simplificado
