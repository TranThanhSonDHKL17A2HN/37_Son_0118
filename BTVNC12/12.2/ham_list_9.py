#bai1
def chuong11_bai1():
 a=[1,2,3]
 b=[1,[2,3]]
 c=[]
 d=[1,2,3][1:]
 print(len(a),len(b),len(c),len(d))

#bai2
def chuong11_bai2():
 team=[['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'],['David', 'Jack', 'Bill', 'Tom', 'Mike', 'Daniel'],['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
 list1=team[2]
 list2=list1[1]
 print('đội trưởng đội yếu nhất:',list2)

#bai3
def chuong11_bai3():
 animals = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
 animal=input('I want to find:')
 print('Number of animals:',len(animals))
 for i in animals:
    if animal==i:
        print('there is',animal,'in list of animals')
        break
 else:
    print('not found')

#bai4
def chuong11_bai4():
 a=[]
 while True:
    b=int(input('nhập giá trị:'))
    a.append(b)
    c=int(input('tiếp tục nhập giá trị?  1:có   0:không'))
    if c==1:
        continue
    if c==0:
        break
 x=int(input('nhập gía trị cần tìm x:'))
 print("list:",a)
 print('tổng các giá trị trong list',sum(a))
 print(x,'xuất hiện',a.count(x),'lần trong list')
 d=[]
 for i in a:
    if i>x:
       d.append(i)
 print('các số lớn hơn',x,'trong list:',d)

#bai5
def chuong11_bai5():
 a=[]
 while True:
     b=int(input('nhập giá trị:'))
     a.append(b)
     c=int(input('tiếp tục nhập giá trị?\n  1:có   0:không\n   '))
     if c==1:
         continue
     if c==0:
         break
 print('list:',a)
 def kiem_tra_so_nguyen_to(x):
  if x<2:
     return False
  else:
     for i in range(2,int(x**0.5)+1):
         if x%i==0:
          return False
     return True
 d=[]
 e=[]
 f=[]
 for i in a:
     if kiem_tra_so_nguyen_to(i):
         d.append(i)
     if i<0:
         e.append(i)
     if i>0:
         f.append(i)
 if len(d)!=0:
     print('các số nguyên tố trong list:',d)
 else:
     print('không có số nguyên tố trong list')
 if len(e)!=0:
     print('các phần tử âm trong list:',e)
     print('trung bình cộng các số âm:',sum(e)/len(e))
 else:
     print('không có phần tử âm trong list')
 if len(f)!=0:
     print('các phần tử dương trong list:',f)
     print('trung bình cộng các số dương:',sum(f)/len(f))
 else:
     print('không có phần tử dương trong list')
 print('giá trị max trong list:',max(a))
 print('giá trị min trong list:',min(a))
 a.sort()
 print('list sắp tăng dần:',a)    

#bai6
def chuong11_bai6():
 a=[74,74,72,72,73,69,69,71,76,71]
 b=[]
 for i in a:
     s=i/0.0254
     b.append(s)
 print(b[0:4])
 print(b[-3:])
 print('chiều cao trung bình:',sum(b)/len(b))
 print('chiều cao lớn nhất:',max(b))
 print('chiều cao nhỏ nhất:',min(b))
 b.sort()
 print('giá trị tăng dần:',b)
 b.reverse()
 print('giá trị giảm dần:',b)

#bai7 
def chuong11_bai7():
 L=[2,5,6,3,2,4,6,3,2,1]
 thresh=int(input('nhập số:'))
 a=[]
 def elementwice_greater_than(L,thresh):
     for i in L:
         if i <= thresh:
             b=False
             a.append(b)
         if i > thresh:    
             b=True
             a.append(b)
     return a
 print(elementwice_greater_than(L,thresh))

#bai8 
def chuong11_bai8():
 nums=[1,2,3,4,7,5,6,8,9]
 def has_lucky_numbers(nums):
     for i in nums:
        if i%7==0:
            print(True)
            break 
     else:
        print(False)
     return
 has_lucky_numbers(nums)

#bai9 
def chuong11_bai9():
 arrival=['adele','fleda','owen','may','mona','gillbert','ford']
 def party_late(arrival,name):
    if (arrival.index(name)+1)==(len(arrival)):
        return False 
    if (arrival.index(name)+1)>(len(arrival)/2):
        return True
    else:
        return False

 print(party_late(arrival,name='gillbert'))
 print(party_late(arrival,name='ford'))
 print(party_late(arrival,name='mona'))

#bai10 
def chuong11_bai10():
 meals_1=['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
 meals_2 =['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
 def menu_is_boring(meals):
     for i in meals:
         if meals.index(i)+1==len(meals):
             return False
         if i==meals[meals.index(i)+1]:
            return True 
 print(menu_is_boring(meals_1))
 print(menu_is_boring(meals_2))
    