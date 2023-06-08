# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:13:54 2023

@author: Avanish Meedimale
"""

import numpy as np
import matplotlib.pyplot as pl

#We want to compute the Inverse Fourier transform B(a)/D(a)

#Discretize time t
t0=-100.
dt=0.001
t=np.arange(t0,-t0,dt)
#Define function
U=1
rho = 1000
mu=0.01
g=9.81
alpha = 0.27
T = (alpha * rho * U **4)/g
D = t - g / U ** 2 - (T * t ** 2) / (rho * U ** 2) - 1j * mu
B= ((rho * U ** 2)*np.exp(-U**4*t**2/(20*g**2)))/(40*g**2/U*4)**(1/2)
f=1000*B/D

#Compute Fourier transform by numpy's FFT function
g=np.fft.ifft(f)
#frequency normalization factor is 2*np.pi/dt
w = np.fft.fftfreq(f.size)*2*np.pi/dt


#In order to get a discretisation of the continuous Fourier transform
#we need to multiply g by a phase factor
g*=dt*np.exp(complex(0,1)*w*t0)/(np.sqrt(2*np.pi))

#Plot Result
pl.plot(w,g)
pl.gca().set_xlim(-10,10)
pl.show()
pl.close()

print("Yes!")
