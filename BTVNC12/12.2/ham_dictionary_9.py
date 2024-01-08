#bai11
def chuong11_bai11():
 tuple="red", "green", 'yellow', 'blue', 'black', "white", "pink", "orange", "red", "blue"
 a=int(input('nhập số từ 0 đến 9:'))
 b=int(input('nhập số từ -1 đến -9:'))
 s_find=input('nhập chuỗi cần tìm:')
 print(tuple)
 print('tuple[',a,']=',tuple[a])
 print('tuple[',b,']=',tuple[b])
 print(s_find,'xuất hiện trong tuple',tuple.count(s_find))

#bai12
def chuong11_bai12():
 tuple_a=3,1,2,4
 tuple_b=5,7,6,8
 tuple_c=tuple_a+tuple_b
 print('tuple_c:',tuple_c)
 a=list(tuple_c)
 a.sort()
 tuple_d=tuple(a) 
 print('tuple_d:',tuple_d)
 print('tuple[3]=',tuple_d[3])
 print('3 phần tử cuối cùng của tuple d',tuple_d[-3:])