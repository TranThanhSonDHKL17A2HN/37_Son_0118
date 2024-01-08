def write_file(filename,cotent):
    with open(filename, 'w') as f:
        f.write(cotent)
        f.close()

f = input("Nhap ten file: ")
content = input("Nhap noi dung can ghi: ")
write_file(f,content)

def read_file(filename):
    with open(filename, 'r') as f:
        a = f.read()
        f.close()
        return a
print("Da ghi noi dung vao tap tin",f)
print(read_file(f))  