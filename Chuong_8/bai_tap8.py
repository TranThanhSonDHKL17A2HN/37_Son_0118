1.1
>>> a, b, c, d = map(float, input("Nhập 4 số cách nhau bằng dấu phẩy: ").split(','))
... 
... 
Nhập 4 số cách nhau bằng dấu phẩy: 24,12,3,11
>>> so_lon_nhat = max(a, b, c, d)
>>> so_nho_nhat = min(a, b, c, d)
>>> print(f"Max = {so_lon_nhat}")
Max = 24.0
>>> print(f"Min = {so_nho_nhat}")
Min = 3.0



1,2
>>> x = int(input("Nhap x: "))
Nhap x: -10
>>> gia_tri_tuyet_doi = abs(x)
>>> print(f"|{x}| = {gia_tri_tuyet_doi}")
|-10| = 10



1.3
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Phương trình bậc nhất: {a}x + {b} = 0")
    print(f"Nghiệm x = {x}")


1.4
a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"Diện tích tam giác = {S}")



1.5
def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
    
nam = 2024
if nam_nhuan(nam):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")




1.6
def calculate_taxi_fare(vehicle_type, distance_km, waiting_minutes):
    if vehicle_type == 4:
        initial_fare = 11000  # Giá mở cửa cho xe 4 chỗ
        price_per_km_within_20km = 12100  # Giá trong phạm vi 20km cho xe 4 chỗ
        price_per_km_beyond_20km = 10000  # Giá từ km thứ 21 trở đi cho xe 4 chỗ
    elif vehicle_type == 7:
        initial_fare = 13000  # Giá mở cửa cho xe 7 chỗ
        price_per_km_within_30km = 14100  # Giá trong phạm vi 30km cho xe 7 chỗ
        price_per_km_beyond_30km = 12000  # Giá từ km thứ 31 trở đi cho xe 7 chỗ
    else:
        return "Loại xe không hợp lệ. Vui lòng chọn 4 hoặc 7 chỗ."

    if distance_km <= 0:
        return "Khoảng cách không hợp lệ."

    if vehicle_type == 4:
        if distance_km <= 0.8:
            fare = initial_fare
        elif distance_km <= 20:
            fare = initial_fare + (distance_km - 0.8) * price_per_km_within_20km
        else:
            fare = initial_fare + 19.2 * price_per_km_within_20km + (distance_km - 20) * price_per_km_beyond_20km
    elif vehicle_type == 7:
        if distance_km <= 0.8:
            fare = initial_fare
        elif distance_km <= 30:
            fare = initial_fare + (distance_km - 0.8) * price_per_km_within_30km
        else:
            fare = initial_fare + 29.2 * price_per_km_within_30km + (distance_km - 30) * price_per_km_beyond_30km

    # Xử lý tiền chờ
    if waiting_minutes > 5:
        waiting_fee = (waiting_minutes - 5) * 800
        fare += waiting_fee

    return fare

# Nhập thông tin và tính cước
vehicle_type = int(input("Nhập loại xe (4 hoặc 7 chỗ): "))
distance_km = float(input("Nhập khoảng cách (km): "))
waiting_minutes = int(input("Nhập thời gian chờ (phút): "))

fare = calculate_taxi_fare(vehicle_type, distance_km, waiting_minutes)
if isinstance(fare, str):
    print(fare)
else:
    print(f"Cước taxi là: {fare} đồng")




1.7
def tinh_tien_dien(kwh):
    if kwh <= 50:
        return kwh * 1678
    elif kwh <= 100:
        return 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        return 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    elif kwh <= 300:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
    elif kwh <= 400:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
    else:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927

# Nhập số lượng kWh tiêu thụ
kwh = float(input("Nhập số kWh tiêu thụ: "))

tien_dien = tinh_tien_dien(kwh)
print(f"Số tiền điện cần thanh toán là: {tien_dien} VND")




1.8
def tinh_tien_thue_phong(ma_loai, so_dem):
    gia_phong = {
        1: 1260000,  # Standard
        2: 1550000,  # Superior Garden View
        3: 1830000,  # Superior Ocean View
        4: 1830000,  # Garden View Bungalow
        5: 2120000,  # Pool View Bungalow
        6: 2120000,  # Family Room
        7: 2540000,  # Beach Front Bungalow
        8: 4800000   # VIP Sea View
    }

    if ma_loai not in gia_phong:
        return "Mã loại phòng không hợp lệ."

    gia_1_dem = gia_phong[ma_loai]

    if so_dem == 1:
        return gia_1_dem
    elif so_dem >= 2 and so_dem <= 3:
        return gia_1_dem * so_dem * 0.75  # Giảm 25% cho 2-3 đêm
    elif so_dem >= 4:
        return gia_1_dem * so_dem * 0.7  # Giảm 30% cho từ 4 đêm trở lên

# Nhập mã loại phòng và số đêm muốn thuê
ma_loai = int(input("Nhập mã loại phòng (1-8): "))
so_dem = int(input("Nhập số đêm muốn thuê: "))

tien_thue_phong = tinh_tien_thue_phong(ma_loai, so_dem)
if isinstance(tien_thue_phong, str):
    print(tien_thue_phong)
else:
    print(f"Tổng tiền thuê phòng là: {tien_thue_phong} VND")



1.9
a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)



8.10
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
s=(x*x+1)**n
print("(S=x*x+1)^n =",s)


8.11
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
A=(x*x+x+1)**n + (x*x-x+1)**n
print("A=(x*x+x+1)^n+(x*x-x+1)^n=",A)


8.12
n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
    print(n, "Không nguyên tố !!!")
else:
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố!!!") 



8.13
# A = tổng các số lẻ nhỏ hơn hoặc bằng n
# B = tổng các số chẵn nhỏ hơn hay bằng n
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3
# E = tổng các cố nguyên tố nhỏ hơn hay bằng n
# F = tổng chuỗi đan dấu
import math
n = int(input("nhập số N: "))
def A(n):
    j = []
    a = 0
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)
A(n)
B(n)
C(n)
D(n)
E(n)
F(n)





8.14
a = int(input("nhập số nguyên N: "))
b = 0
for i in range(1, a+1):
    print("nhập số hạng thứ:", i)
    b1 = int(input())
    b = b + b1
print("tổng",a,"số hạng là ", b)


8.15
a = True
S = 0
while a:
    print("nhập số nguyên N: ")
    b = int(input())
    S = S + b
    if b ==0:
        a = False
        break
print("tổng số hạng vừa nhập là: ",S)




8.16
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while(a*b!=0):
    if a>b:
        a%=b
    else:
        b%=a
print(a+b) 



8.17
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = a*b
for i in range (b, c+1):
    if i%a == 0 and i%b == 0:
        d = i
        break
print(i)




8.18
print("Nhập vào số N lớn hơn 0: ")
n = int(input())
tong = 0
for i in range(1, n):
    if (n % i == 0):
        tong += i
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")






8.19
n = 20
for i in range(n, 0, -1):
    if i % 2 != 0:
        print(i, end= " ")




8.20
def e_mu_x(x, sai_so, n=0, ket_qua=1):
    # Nếu sai số đã đạt được, hoặc n vượt quá một ngưỡng cố định (để tránh lặp vô hạn)
    if abs(x**n / factorial(n)) < sai_so or n > 100:
        return ket_qua
    else:
        n += 1
        ket_qua += x**n / factorial(n)
        return e_mu_x(x, sai_so, n, ket_qua)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

x = float(input("Nhập giá trị của x: "))
sai_so = 1e-4
ket_qua = e_mu_x(x, sai_so)
print(f"e^{x} gần đúng với sai số {sai_so} là: {ket_qua}")
