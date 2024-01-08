def kiem_tra_so_nguyen_to(n):
    so_uoc=0
    for i in range(1,n+1):
        if n%i==0:
            so_uoc+=1
    if so_uoc==2:
        return True
    return False
n=int(input("Nhập số cần kiểm tra: "))
print(kiem_tra_so_nguyen_to(n))