while True:
 try:
  a=int(input("giá trị cạnh thứ nhất:"))
  b=int(input("giá trị cạnh thứ hai:"))
  c=int(input("giá trị cạnh thứ ba:"))
  if a<=0 or b<=0 or c<=0:
     raise TypeError ("Vui lòng nhập giá trị lớn hơn 0!!!")
  if a+b<=c or a+c<=b or b+c<=a:
     raise TypeError ("Vui lòng nhập lại giá trị!!!")        
 except ValueError as f:
    print("Vui lòng nhập giá trị là số nguyên dương!!!")
 except TypeError as q:
     print(q)
 else:
     q=int(a+b+c)/2
     import math
     s=math.sqrt(q*(q-a)*(q-b)*(q-c))
     print("diện tích tam giác:",s)
     break