def kiem_tra_ma_zip(z):
    if len(z)==6 and z.isdigit()==True:
        return True
    else:
        return False
z=input("Nhập mã zip :")
print(kiem_tra_ma_zip(z))  