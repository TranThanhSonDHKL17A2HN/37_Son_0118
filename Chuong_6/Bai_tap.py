#Bài tập 1.1
characters = {
    'h': ["**  **", "**  **", "******", "**  **", "**  **"],
    'e': ["******", "**    ", "******", "**    ", "******"],
    'l': ["**    ", "**    ", "**    ", "**    ", "******"],
    'o': [" ****** ", " **  **", " **  **", " **  **", " ****** "]
}
text = "hello"
for row in range(5):
    for char in text:
        print(characters[char][row], end="  ") 
    print() 

1.2
x = 10
y = 5
Tổng = x+y
Hiệu = x-y
Tích = x*y
Thương = x/y
print(f"x = {x} , y = {y}")
print(f"Tổng x+y = {Tổng} ")
print(f"Hiệu x-y = {Hiệu}")
print(f"Tích x*y = {Tích}")
print(f"Thương x/y = {Thương}")



1.3
ten_hang = "Sữa hộp vinamilk"
so_luong = 5
don_gia = 25000
tien_phai_tra = don_gia*so_luong
print(f"Tên hàng: {ten_hang}")
print(f"Số lượng: {so_luong}")
print(f"Đơn giá: {don_gia}")
print((f"Tiền phải trả: {tien_phai_tra} vnđ"))



1.4
#Yêu cầu 1
result = (5 - 3)//2
print(result)

#Yêu cầu 2
result = 8 - (3*2) - (1 + 1)
print(result)




1.5
>>> so_luong = int(input("Nhập số lượng: "))
Nhập số lượng: 100
>>> don_gia = float(input("Nhập đơn giá: "))
Nhập đơn giá: 5000
>>> thanh_tien = so_luong * don_gia
>>> print(f"Thành tiền = {so_luong} * {don_gia} = {thanh_tien}")
Thành tiền = 100 * 5000.0 = 500000.0



1.6
alice_candies = 121
bob_candies = 77
carol_candies = 109
total_candies = alice_candies + bob_candies + carol_candies
per_person_candies = total_candies // 3
candies_remainder = total_candies % 3
print(f"Số lượng kẹo dư: {candies_remainder}")



1.7
>>> # Nhập độ C
... celsius = float(input("Nhập độ C: "))
Nhập độ C: 27
>>> 
... # Chuyển đổi sang độ F
... fahrenheit = (celsius * 9/5) + 32
>>> 
... # Hiển thị kết quả với 2 chữ số thập phân
... print(f"{celsius:.2f} độ C = {fahrenheit:.2f} độ F")
27.00 độ C = 80.60 độ F



1.8
>>> s1 = input("Nhập chuỗi s1: ")
Nhập chuỗi s1: hello
>>> s2 = input("Nhập chuỗi s2: ")
... 
Nhập chuỗi s2: Python
>>> s3 = input("Nhập chuỗi s3: ")
... 
Nhập chuỗi s3: programing laguage
>>> index = int(input("Nhập chỉ mục index: "))
... 
Nhập chỉ mục index: 2
>>> print(f"Chiều dài của chuỗi s1: {len(s1)}")
Chiều dài của chuỗi s1: 5
>>> print(f"Chiều dài của chuỗi s2: {len(s2)}")
... 
Chiều dài của chuỗi s2: 6
>>> print(f"Chiều dài của chuỗi s3: {len(s3)}")
... 
Chiều dài của chuỗi s3: 18
>>> print(f"Lặp lại chuỗi s2 2 lần với nội dung 'Python': {s2_repeated}")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(f"Lặp lại chuỗi s2 2 lần với nội dung 'Python': {s2_repeated}")
NameError: name 's2_repeated' is not defined
>>> s2_repeated = s2 + "Python" + s2
... 
>>> print(f"Lặp lại chuỗi s2 2 lần với nội dung 'Python': {s2_repeated}")
Lặp lại chuỗi s2 2 lần với nội dung 'Python': PythonPythonPython
>>> s4 = s1[index:]
>>> KeyboardInterrupt
>>> print(f"Chuỗi s4 từ index {index} đến hết: {s4}")
Chuỗi s4 từ index 2 đến hết: llo




1.9
lai_suat = float(input("Nhập lãi suất một năm (%): "))
Nhập lãi suất một năm (%): 7.6
>>> so_tien_gui = float(input("Nhập số tiền gửi (VNĐ): "))
... 
Nhập số tiền gửi (VNĐ): 10000000
>>> so_thang_gui = int(input("Nhập số tháng gửi: "))
... 
Nhập số tháng gửi: 6
>>> lai = (so_tien_gui * so_thang_gui) * (lai_suat / 100 / 12)
>>> tong_so_tien = so_tien_gui + lai
... 
>>> print(f"Tiền lãi = ({so_tien_gui} * {so_thang_gui}) * ({lai_suat} / 100 / 12) = {lai} VNĐ")
Tiền lãi = (10000000.0 * 6) * (7.6 / 100 / 12) = 380000.0 VNĐ
>>> print(f"Tiền vốn + lãi = {so_tien_gui} + {lai} = {tong_so_tien} VNĐ")
Tiền vốn + lãi = 10000000.0 + 380000.0 = 10380000.0 VNĐ