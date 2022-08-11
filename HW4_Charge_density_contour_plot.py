# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 06:51:09 2022

@author: dag5
"""

from numpy import empty,zeros,max
from pylab import imshow,gray,show,colorbar,contour
import timeit

# Constants
M = 100		# Grid squres on a sid
target = 1e-6   # Target accuracy
V=1.0
alpha = 1.9     # SOR mixing parameter


eps0 = 1.0      # the permittivity of empty sapce
h = 100/M       # grid spacing

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phi[0,:] = V

# Create array to hold charge density
rho = zeros([M+1,M+1], float)
for i in range(M+1):
    for j in range(M+1):
        if j == 20:
            if 20 <= i and i <= 80:
                rho[i,j] = 2.0
        if j == 80:
            if 20 <= i and i <= 80:
                rho[i,j] = -2.0
    
start = timeit.default_timer()

#Main loop for adjusting phi at each point within the grid
delta = 1.0

iterations = 1
while delta > target:
    
    #Initial placeholder value for delta max. With each iteration delta 
    #will become delta max until it is less than the target
    delta_max = 0
    
    for i in range(1,M):
        for j in range(1,M):
            #The phi[i-1,j] and phi[i,j-1] terms will have already been calculated during
            #The loop because the indices are less than those the loop is currently
            #On. This is why they are labeled phi_NEW[i,j-1] / phi_NEW[i-1,j] in
            #The algorithm for the SOR and Gauss Seidel Methods.
            #The elements with greater indices are called phi_OLD because the elements
            #In those indices have not yet been updated by the loop
            phi_star = (1/4)*(phi[i-1,j] + phi[i,j-1]+ phi[i+1,j] + phi[i, j+1]) + ((h**2)/(4*eps0))*rho[i,j]
            #Again this uses the current value of phi[i,j] which is why it is phi_OLD[i,j]
            #In the algorithm written out.
            delta_phi = phi_star - phi[i,j]
            #Finally updating phi[i,j]
            phi[i,j] = phi[i,j] + alpha*delta_phi
            
            # Updates delta max to be the largest delta_phi yet obtained.
            if abs(delta_phi) > delta_max :
               delta_max = abs(delta_phi)
               
    #Updates delta to be the maximum delta obtained over the last run of the
    #double for loop. 
    delta = delta_max

    iterations += 1
    if iterations%100 == 0 :
       print("...  iteration #%d ..." %(iterations))
       
time = timeit.default_timer()-start
print("Total Computing Time:%7.2f seconds; Total iterations: %d" %(time, iterations))
       
#Because there is the term with a factor of rho in the calculation for phi_star,
#Phi has the greatest values in the highest-density areas (that being the locations
#of the two plates)
contour(phi)
imshow(phi)
colorbar()
show()
       

    
            