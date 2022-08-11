# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 08:22:46 2022

@author: Drew
"""

from numpy import loadtxt, copy
from numpy.fft import rfft,irfft 
from pylab import plot,show, zeros
from scipy.fft import dct, idct

"""
 Load data file 'dow.txt' and plot the data 
"""
y = loadtxt("dow2.txt",float)
plot(y,"b-") 


"""
Calculate the coefficients of the discrete Fourier transform 
of the data using the function rfft from numpy.fft, 
which produces an array of N/2+1 complex numbers. 
"""
c = rfft(y)
#This is the discrete cosine transform part from question 2
d = dct(y)


"""
Set all but the first 10% of the elements of this array to zero 
let new array be c_new.
"""
c_new = zeros(len(c),complex)
c_new[0:len(c)//50] = c[0:len(c)//50]
#Perform same thing for the d array generated using the discrete cosine transforms
d_new = zeros(len(d),complex)
d_new[0:len(d)//50] = d[0:len(d)//50]



"""
Calculate the inverse Fourier transform of the resulting array, zeros 
and all, using the function irfft, 
"""
y_irfft = irfft(c_new)
y_dct = idct(d_new)

"""
plot it on the same graph as the original data. 
"""
plot(y_irfft,"r-")
plot(y_dct, 'g-')


show()