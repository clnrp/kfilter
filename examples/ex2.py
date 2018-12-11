#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kfilter.simplify import *
from sympy import *

dt = Symbol('dt')
x0, v0 = symbols('x0, v0')
Q00,Q11 = symbols('Q_x, Q_v')

# x = x0 + v0*dt + 1/2*a*dt**2
# v = v0 + a*dt

x = Matrix([[x0],[v0]]) # vetor de estados
A = Matrix([[1, dt], [0, 1]]) # matriz de transição de estados
B = Matrix([[1/2.*dt**2], [dt]]) # matriz de entradas de controle
H = Matrix([[1, 0]]) # modelo de observação
Q = Matrix([[Q00, 0], [0, Q11]])*dt # covariância do ruído do processo
u,z = symbols('a,x_m')

# imprimir dados
print(x)
print(A)
print(B)
print(u)
print(H)

simplify = Simplify(A,x,B,u,z,H)
simplify.setQ(Q)
simplify.compute() # calcular simplificações
simplify.printq()  # imprimir filtro simplificado
