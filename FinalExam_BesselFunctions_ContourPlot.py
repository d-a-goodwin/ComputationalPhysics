# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:01:17 2022

@author: Drew
"""
from gaussxw import gaussxwab
from math import cos, sin, pi
from pylab import plot,show,legend,imshow,gray,colorbar,contour,xlabel,ylabel,figure
from numpy import arange

def f(theta,m,x):
    
    return cos(m*theta - x*sin(theta))

"""I chose to use the Guassian quadrature. The algorithm chooses random points
from the range provided and assigns weights to them to be used in the summation
In the summation, the integrand function values at these random points is multiplied by the weights, and
added to the total sum."""
def J(m,x):
    
    N = 100
    theta,w = gaussxwab(0,pi,N)
    total = 0
    for i in range(N):
        total += w[i]*f(theta[i],m,x)
    
    return total/pi

"""Taking a small range of points near x=0 and proving that J1 at these points
is 1/2 x. This is because by hint a, the limit of J1/x (rise/run) as x approaches
0 is 1/2. So if x is near zero, J1 at that point should be approximately 1/2 of x."""

nearzero = arange(0,0.2,0.01)
J1s = [J(1,x) for x in nearzero]
#Comparing the two lists shows that the corresponding J1s are consistently about 1/2 of the Xes.
print("Xes near 0: " , nearzero)
print("Corresponding J1s: ", J1s)
    
bessel_m0 = []
bessel_m1 = []
bessel_m2 = []

for x in range(0,21):
    
    bessel_m0.append(J(0,x))
    bessel_m1.append(J(1,x))
    bessel_m2.append(J(2,x))

plot(range(0,21),bessel_m0,label="Bessel functions with m=0", color="blue")
plot(range(0,21),bessel_m1,label="Bessel functions with m=1", color="red")
plot(range(0,21),bessel_m2,label="Bessel functions with m=2", color="black")
xlabel("x inputted into Bessel functions")
ylabel("Jm(x)")
legend()   
show()

def I(lamb,r):
    
    k = 2*pi/lamb
    
    return (J(1,k*r)/(k*r))**2
    
x = arange(-10**-6,10**-6,10**-7)
y = arange(-10**-6,10**-6,10**-7)

I_arr = []

for i in range(len(x)):
    
    I_arr.append([])
    
    for j in range(len(y)):
        
        r = (x[i]**2 + y[j]**2)**(1/2)
        
        if r <= 10**-6:
            
            I_arr[i].append(I(500*10**-9,r))
        
        else:
        
            I_arr[i].append(0)
            
#print(I_arr)
            

contour(I_arr)
imshow(I_arr,cmap="gist_heat")
colorbar()
show()
        
        
    

    
    
    
    
    

    
    