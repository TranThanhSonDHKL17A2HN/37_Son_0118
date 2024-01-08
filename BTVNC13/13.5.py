import csv
def read_csv(filename):
    f=open(filename)
    for row in csv.reader(f):
        print(row)
    f.close()
    
f = input("Nhap ten tap tin: \n")
print("Noi dung tap tin: ")
read_csv(f)