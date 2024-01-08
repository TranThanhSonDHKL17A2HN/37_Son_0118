import math
print("Nhập n:")
n=int(input())
print("Nhập x:")
x=float(input())
A=math.pow(math.pow(x,2)+x+1,n)+math.pow(math.pow(x,2)-x+1,n)
print("A=(x*x +x+1)^n + (x*x -x + 1)^n =",A)