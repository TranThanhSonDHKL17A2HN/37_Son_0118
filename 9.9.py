import math
sht =lambda r:math.pi*math.pow(r,2)
pht =lambda r:2*math.pi*r
scn=lambda a,b:a*b
pcn=lambda a,b:2*(a+b)
r=float(input("Bán kính r = "))
a=float(input("Chiều dài hình chữ nhật a = "))
b=float(input("Chiều rộng hình chữ nhật b = "))
print("S hình tròn = %0.2f"%sht(r))
print("P hình tròn = %0.2f"%pht(r))
print("S hình chữ nhật = %0.2f"%scn(a,b))
print("P hình chữ nhật = %0.2f"%pcn(a,b))