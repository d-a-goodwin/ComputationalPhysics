# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:43:11 2022

@author: Drew
"""

from random import random
from numpy import exp

def f(x):
    return x**(-0.5)/(exp(x)+1)
    
def importance_sampling(a,b,N):
    total_sum = 0
    for i in range(1,N):
        x = random()*b
        if x > 0:
            total_sum += f(x)
    
    return total_sum/N

print(importance_sampling(0,1,1000000))