#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kfilter.simplify import *
from sympy import *

dt = Symbol('dt')
x0, v0 = symbols('x0, v0')
Q00,Q11 = symbols('Q_x, Q_v')
Q = Matrix([[Q00, 0], [0, Q11]])*dt

x = Matrix([[x0],[v0]])
A = Matrix([[1, dt], [0, 1]])
B = Matrix([[1/2.*dt**2], [dt]])
H = Matrix([[1, 0]])
u,z = symbols('a,x_m')

print(x)
print(A)
print(B)
print(u)
print(H)

simplify = Simplify(A,x,B,u,z,H)
simplify.setQ(Q)
simplify.compute()
simplify.printq()
