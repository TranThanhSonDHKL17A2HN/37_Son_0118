ng=int(input('Nhập ngày: '))
t=int(input('Nhập tháng: '))
n=int(input('Nhập năm: '))
from datetime import datetime
a=datetime(n,t,ng)
print("Ngày tháng năm vừa nhập: ",a.strftime("%d-%m-%Y"))
import calendar
if calendar.isleap(n)==True:
    print("Năm",n,"là năm nhuận")
else:
    print("Năm",n,"không phải là năm nhuận")    
if calendar.weekday(n,t,ng)==0:
    print(a.strftime("%d-%m-%Y"),"là thứ 2")
elif calendar.weekday(n,t,ng)==1:
    print(a.strftime("%d-%m-%Y"),"là thứ 3") 
elif calendar.weekday(n,t,ng)==2:
    print(a.strftime("%d-%m-%Y"),"là thứ 4")
elif calendar.weekday(n,t,ng)==3:
    print(a.strftime("%d-%m-%Y"),"là thứ 5")
elif calendar.weekday(n,t,ng)==4:
    print(a.strftime("%d-%m-%Y"),"là thứ 6")
elif calendar.weekday(n,t,ng)==5:
    print(a.strftime("%d-%m-%Y"),"là thứ 7")
else:
    print(a.strftime("%d-%m-%Y"),"là chủ nhật")
print("Số ngày trong tháng",t,"là:",calendar.monthrange(n,t))