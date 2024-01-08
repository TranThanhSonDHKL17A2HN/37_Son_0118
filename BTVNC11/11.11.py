a=['red','green','yellow','blue','black','white','pink','orange','red','blue']
print("Tuple :",a)
x=int(input('Nhập số từ 0 đến 9: '))
y=int(input('Nhập số từ -1 đến -9: '))
z=input('Nhập chuỗi cần tìm: ')
print("Tuple[",x,"] =",a[x])
print("Tuple[",y,"] =",a[y])
print(z,"xuất hiện trong tuple",a.count(z),"lần")