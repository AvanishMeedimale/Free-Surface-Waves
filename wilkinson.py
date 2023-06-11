# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:46:00 2023

@author: Avanish Meedimale
"""

import numpy as np
import matplotlib.pyplot as plt

B=np.linspace(0,1,16)
B.shape=(8,2)
print("ey")
#A=np.random.rand(3,5)


wilkinson_coeffs = [ 1,
                  -210,
                 20615,
              -1256850,
              53327946,
           -1672280820,
           40171771630,
         -756111184500,
        11310276995381,
      -135585182899530,
      1307535010540395,
    -10142299865511450,
     63030812099294896,
   -311333643161390640,
   1206647803780373360,
  -3599979517947607200,
   8037811822645051776,
 -12870931245150988800,
  13803759753640704000,
  -8752948036761600000,
   2432902008176640000]

figure, axis = plt.subplots(3)
plt.suptitle('ah')

for i in range(6,9):
    eps=10**(-i)
    A=eps*np.ones(21)
    wilkinson_coeffs=np.array(wilkinson_coeffs)
    pert=A+wilkinson_coeffs
    pert_roots=np.roots(pert)
    x=np.arange(1,20,1)
    y=np.zeros(19)
    axis[i-6].plot(x, y, 'ro', np.real(pert_roots), np.imag(pert_roots),'kx', markersize=7.0)