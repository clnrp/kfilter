#!/usr/bin/python
# encoding: utf-8

from kfilter.kalman import *
from math import *
from drawnow import *
from numpy import *
import matplotlib.pyplot as plt
import time
import serial

RAD_TO_DEG = 180 / pi
DEG_TO_RAD = pi / 180

dt = 0.01

# angle = angle0 + (newVelocity - bias)*dt
# bias  = bias

x0 = matrix([[0], [0]])  # vetor de estados
A = matrix([[1, -dt], [0, 1]])  # matriz de transição de estados
B = matrix([[dt], [0]]) # matriz de entradas de controle
P = matrix([[0, 0], [0, 0]]) # matriz de covariância
H = matrix([[1, 0]]) # modelo de observação
Q0 = matrix([[0.001, 0], [0, 0.003]]) # covariância do ruído do processo
R=0.03 # covariância do ruído da observação

#kalman_pitch = Kalman(A,x0,B,H,Q0,R,P)
kalman_roll = Kalman(A,x0,B,H,Q0,R,P)

def getAccelRollPitch(ax, ay, az):
    roll = atan2(ax, abs(az)) * RAD_TO_DEG
    # pitch = atan2(-ay, abs(az)) * RAD_TO_DEG
    pitch = atan(-ay / sqrt(ax * ax + az * az)) * RAD_TO_DEG
    return [roll, pitch]

def plotValues(): # plotar dados
    plt.title('mpu6050')
    plt.ylabel('Angulo')
    plt.ylim(-100, 100)
    plt.plot(data_raw, 'rx-', label='Accel')
    plt.plot(data_kalman, 'bx-', label='kalman')
    plt.legend(loc='upper right')

ser = serial.Serial("/dev/ttyUSB0", 9600)

plt.ion()
data_raw = range(0,26)
data_kalman = range(0,26)

cnt = 0
t0 = time.time()
t = 0
while True:
    try:
       cnt += 1
       data = ser.readline() # obter os dados pela serial
       data = data.strip()

       [ax, ay, az, gx, gy, gz] = data.split(',') # separar os dados
       [ax, ay, az, gx, gy, gz] = [float(ax),float(ay),float(az),float(gx),float(gy),float(gz)]
       print(ax,ay,az)

       t1 = time.time()
       dt = t1 - t0
       t0 = t1

       A = matrix([[1, -dt], [0, 1]]) # atualizar matriz de transição de estados
       B = matrix([[dt], [0]]) # atualizar matriz de entradas de controle
       kalman_roll.setA(A)
       kalman_roll.setB(B)
       kalman_roll.setQ(Q0*dt) # atualizar covariância do ruído do processo

       roll, pitch = getAccelRollPitch(ax, ay, az)
       k_roll = kalman_roll.compute(-gy, roll).item(0) # filtrar o angulo usando a aceleração e a velocidade angular

       print(roll, k_roll)
       data_raw.append(roll)
       data_raw.pop(0)
       data_kalman.append(k_roll)
       data_kalman.pop(0)
       drawnow(plotValues) # plotar dados
    except Exception as ex:
       print(str(ex))


