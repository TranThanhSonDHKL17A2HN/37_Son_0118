def write_name_and_phone(file,name_and_phone):
    with open(file, 'a', newline = '') as f:
        write = csv.writer(f)
        write.writerow(name_and_phone)
        f.close()


x = input("Nhap ten tap tin: ") 



def name(n):
    while True:
        ten = input("Nhap ten: ")
        so = input("Nhap so: ")
        name_and_phone = [ten, so]
        write_name_and_phone(x,name_and_phone)
        

import csv
def read_csv(file):
    with open(file, 'r', newline = '', encoding = 'utf-8') as f:
        for line in csv.reader(f):   
            return line
        

print(read_csv(x))