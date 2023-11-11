1.1
>>> x = int(input("Nhập giá trị x: "))
Nhập giá trị x: 6
>>> S = 1 + x + (x**3) / 3 + (x**5) / 5
... 
>>> print(f"S = 1 + {x} + ({x}^3 / 3) + ({x}^5 / 5) = {S:.1f}")
... 
S = 1 + 6 + (6^3 / 3) + (6^5 / 5) = 1634.2


1.2
result = 1 + 2
print('result =', result)
original_result = result
result = result - 1
print('result =', result)
original_result = result
result = result * 2
original_result = result
print('result =', result)
result = result ** 3
original_result = result
print('result =', result)
result = result + 8
original_result = result
print('result =', result)
result = result % 7
original_result = result
print('result =', result)
result = result // 2
original_result = result
print('result =', result)
Vay ket qua = 1


1.3
result = 5
print('result =', result)
result = -1
print('result =', result)
result += 3
print('result =', result)
result = -result
print('result =', result)
result = True
print('not result =', not result)
Ket qua la False

1.4
x = 10
y = 4
print('x =%d, y =%d'%(x,y))
enquivelence = x==y
print('x==y is', enquivelence)
enquivelence = x!=y
print('x!=y is', enquivelence)
enquivelence = x>y
print('x>y is', enquivelence)
x = 8
y = 9
print('x =%d, y = %d'%(x,y))
enquivelence = x>=y
print('x>=y is', enquivelence)
enquivelence = x<y
print('x<y is', enquivelence)
enquivelence = x<=y
print('x<=y is', enquivelence)

#Ket qua :
Voi x = 10 , y = 4
x==y Flase
x!y True
x>y True
Voi x = 8 , y = 9
x>=y False
x<y True
x<=y True


1.5
x = 15
y = 12
print('Binary of x =', bin(x), 'Binary of y =', bin(y))
print('x & y =', bin(x & y))
print('x / y =', bin(x | y))
print('x ^ y =', bin(x ^ y))
print('~x', bin(~x))
print('x << 2 =', bin(x << 2))
print('y >> 2', bin(y >> 2))

#Ket qua
Binary of x = 0b1111 Binary of y = 0b1100
x & y = 0b1100
x / y = 0b1111
x ^ y = 0b11
~x -0b10000
x << 2 = 0b111100
y >> 2 0b11




1.6
>>> x= True
>>> y= False
>>> print("x and y:",x and y)
x and y: False
>>> print("x or y:",x or y)
x or y: True
>>> print("not x:",not x)
not x: False
>>> print("x is y:",x is y)
x is y: False
>>> print("x is not y:",x is not y)
x is not y: True



1.7
def doi_tien(money):
    menh_gia = [500000, 200000, 100000, 50000]
    so_to_tien = []
    tien_du = money

    for menhgia in menh_gia:
        so_to = tien_du // menhgia
        if so_to > 0:
            so_to_tien.append((menhgia, so_to))
            tien_du %= menhgia

    return so_to_tien, tien_du

so_tien_goc = 1375000
so_to_tien, tien_du = doi_tien(so_tien_goc)

print(f"Số tiền muốn đổi: {so_tien_goc}")
for menhgia, so_to in so_to_tien:
    print(f"Số tờ {menhgia}: {so_to} ")
print(f"Tiền còn lại: {tien_du}")
