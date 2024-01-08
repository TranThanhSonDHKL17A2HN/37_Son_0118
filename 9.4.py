import math
def tinh_S(n,x):
    S = math.pow((x*x+1),n)
    return S
n = float(input('n = '))
x = float(input("x = "))       
S = tinh_S(n,x)
print("S = %0.2f"%S)   