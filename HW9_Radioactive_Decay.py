# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:18:23 2022

@author: Drew

"""

import numpy

from numpy import ones, zeros
from random import random
from math import log
from pylab import plot, legend, xlabel, ylabel

#Begin with an array of only 1s. 1s represent 213Bi
N_isotopes = 10000
N_seconds = 25000
isotopes = ones(N_isotopes)
#This array is made to store how many seconds each isotope has existed
#in order to calculate their individual decay probabilities at each
#time step
lives = zeros(N_isotopes)

arr_209Bi = zeros(N_seconds)
arr_213Bi = zeros(N_seconds)
arr_209Pb = zeros(N_seconds)
arr_209Tl = zeros(N_seconds)
tot_209Bi = 0
tot_213Bi = N_isotopes
tot_209Pb = 0
tot_209Tl = 0


t = 0
time = range(0,N_seconds)

for i in range(len(time)):
    
    
    
    for j in range(len(isotopes)):
        
        #2 REPRESENTS 209PB
        if isotopes[j]==2:
            #Calculate the probability of decay given how long this isotope has existed
            decay_probability = (2**(-lives[j]/198)) * log(2)/198
            if random() < decay_probability:
                #If 209Pb decays, it becomes 209Bi, so set the value of isotopes[j] to 4
                #And set the life of the particle to 0
                isotopes[j] = 4
                tot_209Pb -= 1
                tot_209Bi += 1
                lives[j] = 0
            else:
                lives[j] += 1
                
        #3 REPRESENTS 209TL
        elif isotopes[j]==3:
            #Calculate the probability of decay given how long this isotope has existed
            decay_probability = (2**(-lives[j]/132)) * log(2)/132
            if random() < decay_probability:
                #If the 209Tl decays, it becomes 209Pb so set isotopes[j] to 2 and lives[j] to 0
                tot_209Pb += 1
                tot_209Tl -= 1
                isotopes[j] = 2
                lives[j] = 0
            else:
                lives[j] += 1
        
        #1 REPRESENTS 213BI
        elif isotopes[j]==1:
            #Calculate the probability of decay given how long this isotope has existed
            decay_probability = (2**(-lives[j]/2760)) * log(2)/2760
            if random() < decay_probability:
                #If the random number is less than probability of Tl, add a Tl
                #Otherwise add a 209Pb
                if random() < 0.0209:
                    tot_213Bi -= 1
                    tot_209Tl += 1
                    isotopes[j] = 3
                    lives[j] = 0
                else:
                    tot_209Pb += 1
                    tot_213Bi -= 1
                    isotopes[j] = 2
                    lives[j] = 0
            else:
                lives[j] += 1
                    
    arr_209Bi[i] = tot_209Bi
    arr_209Pb[i] = tot_209Pb
    arr_209Tl[i] = tot_209Tl
    arr_213Bi[i] = tot_213Bi
        
        
plot(time,arr_209Bi, label="209Bi")
plot(time,arr_209Pb, label="209Pb")
plot(time,arr_209Tl, label="209Tl")
plot(time,arr_213Bi,label = "213Bi")
legend()
xlabel("Number of seconds elapsed")
ylabel("Number of isotope (see legend)")
                
                
            
        
            
        
        
        
        
            
    
