mylist=[]
while True:
    val=int(input("Nhập giá trị : "))
    a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
    mylist.append(val)
    if a==0:
        x=int(input("Nhập giá trị cần tìm x:"))
        break
print('List:',mylist) 
print('Tổng các giá trị trong list:',sum(mylist))
print(x,'xuất hiện',mylist.count(x),'trong list')
if max(mylist)==x:
    print(x,'lớn hơn tất cả các số trong list')
else:
    print(x,'không lớn hơn tất cả các số trong list')
newlist=[int(i) for i in mylist if int(i)>x]
print('Các số lớn hơn',x,'trong list',newlist)