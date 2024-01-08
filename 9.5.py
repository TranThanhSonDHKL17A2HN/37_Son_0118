import math
def tinh_A(n,x):
    A=math.pow(((x*x)+x+1),n)+math.pow(((x*x)-x+1),n)
    return A
n=float(input('n = '))
x=float(input("x = "))       
A = tinh_A(n,x)
print("A = %0.2f"%A) 