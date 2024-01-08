def sign(x):
    if x<0:
        return "-1"
    elif x>0:
        return "1"
    elif x==0:
        return "0"
x=int(input("Nhập x : "))
print("sign(",x,")=",sign(x))