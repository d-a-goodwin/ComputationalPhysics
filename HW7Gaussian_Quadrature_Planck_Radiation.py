# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 08:11:49 2022

@author: Drew
"""

from pylab import plot,subplot,bar,show,loglog,\
                  xlabel, ylabel, xlim,ylim, legend, title
from numpy import exp, array, abs, pi, sin, ones, inf
from gaussxw import gaussxwab

#Constants
T = 300.0
KB = 1.38064852 * 10**-23
c = 3 * 10**8
Hbar = 1.055 * 10**-34

def f(k):
    return (k**3)/(exp(k)-1)

def quadrature(x,w):
    total = 0.0
    for i in range(len(x)):
        total += w[i]*f(x[i])
        

    return total

#Questions 3 and 4

Ns = [2**i for i in range(1,15)]
solutions_func_of_N = []

for N in Ns:
    x,w = gaussxwab(0,1000000, N)
    solutions_func_of_N.append(quadrature(x,w)*(KB**4)*(T**4)/(4*(pi**2)*(c**2)*(Hbar**3)))
    
print(solutions_func_of_N)
    
plot(Ns, solutions_func_of_N)
title("Total energy of Planck radiation by grid points used in summation")
xlabel("Number of grid points used")
ylabel("Total Energy of radiation (J)")
show()

#Question 5: N is held constant

N = 2**14

Ts = range(1,5001,50)
solutions_func_of_T = []

x,w = gaussxwab(0,1000000,N)
for T in Ts:
    solutions_func_of_T.append(quadrature(x,w)*(KB**4)*(T**4)/(4*(pi**2)*(c**2)*(Hbar**3)))
    
plot(Ts, solutions_func_of_T)
title("Total energy of Planck radiation by temperature of object")
xlabel("Object Temperature (K)")
ylabel("Total Energy of radiation (J)")
show()

#Question 6

#Going to calculate stefan - boltzmann constant using each T and W
stefboltz = []
for i in range(len(Ts)):
    stefboltz.append(solutions_func_of_T[i]/(Ts[i]**4))
    
stefboltzconst = sum(stefboltz)/len(stefboltz)
print("Stefan-Boltzmann constant: ", stefboltzconst)
