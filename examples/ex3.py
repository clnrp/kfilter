#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kfilter.simplify import *
from sympy import *

dt = Symbol('dt')
angle,bias = symbols('angle, bias')
Q00,Q11 = symbols('Q_angle, Q_bias')
Q = Matrix([[Q00, 0], [0, Q11]])*dt

x = Matrix([[angle], [bias]])
A = Matrix([[1, -dt], [0, 1]])
B = Matrix([[dt], [0]])
u,z = symbols('newVelocity,newAngle')
H = Matrix([[1, 0]])

print(x)
print(A)
print(B)
print(u)
print(H)

simplify = Simplify(A,x,B,u,z,H)
simplify.setQ(Q)
simplify.compute()
simplify.printq()
