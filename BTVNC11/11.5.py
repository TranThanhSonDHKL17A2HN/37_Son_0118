mylist=[]
while True:
    val=int(input("Nhập giá trị : "))
    a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
    mylist.append(val)
    if a==0:
        break
print('List:',mylist)
am=[int(i) for i in mylist if int(i)<0]
print('Các phần tử âm trong list:',am)
print('Trung bình cộng các phần tử âm',sum(am)/len(am))
duong=[int(i) for i in mylist if int(i)>0]
print('Các phần tử dương trong list:',duong)
print('Trung bình cộng các phần tử dương',sum(duong)/len(duong))
print('Giá trị max trong list',max(mylist))
print('Giá trị min trong list',min(mylist))
mylist.sort()
print('List sắp tăng dần:',mylist)