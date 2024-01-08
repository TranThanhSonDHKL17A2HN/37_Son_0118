def kiem_tra_so_hoan_hao(n):
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    if tong_uoc==n:
        return True
    else:
        return False
n=int(input("Nhập số nguyên dương n: ")) 
if kiem_tra_so_hoan_hao(n):
    print(n,"là số hoàn hảo")
else:
    print(n,"không là số hoàn hảo")  