from math import *
from sympy import *

z = Symbol('x')

fx = input("Enter the expression : ")
d = diff(fx)
f1x = lambdify(z, d, "math")

x=0
if("log" in fx):
    x=1

a=eval(fx)
x=x+1
b=eval(fx)
if (a<0 and b>0) or (a>0 and b<0):
    print("\nRoots lie between ({},{})".format(x-1,x))
else:
    while a!=0 and b!=0 :
        if (a<0 and b>0) or (a>0 and b<0):
            break
        x=x+1
        a=eval(fx)
        if (a<0 and b>0) or (a>0 and b<0):
            break
        x=x+1
        b=eval(fx)
    print("\nRoots lie between ({},{})".format(x-1,x))
    

p=x-1
q=x
i=0
h=0
float(h)
x=(p+q)/2

while round(h,4)!=round(x,4):
    h=x
    i=i+1
    print("\n{} Approximation :- ".format(i))
    xa=x-(eval(fx)/f1x(x))
    print("x{} = {}".format(i,xa))
    x=xa
    
print("\nSince, x{0:.5f} ~ x{0:.5f} ".format(h,x))
print("\nTherefore, the required root is {0:.5f}.".format(h)) 

