b=[]
while True:
    try:
      a=int(input("nhập số"))
      b.append(a)  
      if a<=0:
            raise TypeError ("Lỗi số âm!!!")
      if len(b)>=4 and b[-1]==b[-2] and b[-1]==b[-3] and b[-1]==b[-4]:
            raise TypeError ("Lỗi nhập lặp số!!!")
      if len(b)>=5 and b[-1]%2==0 and b[-2]%2==0 and b[-3]%2==0 and b[-4]%2==0 and b[-5]%2==0:
            raise TypeError ("Lỗi nhập chẵn!!!")
    except ValueError :
        print("Lỗi nhập số!!!")
        b.pop(-1)
    except TypeError as f:
        print(f)
        b.pop(-1)