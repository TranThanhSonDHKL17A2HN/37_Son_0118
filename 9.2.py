can = ["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
chi = ["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
def tinh_nam_am_lich(n):
    i=n%10
    j=n%12
    return i,j
n = int(input("Nhập năm: "))
i,j = tinh_nam_am_lich(n)
print("Năm",n,"lịch âm là năm:",can[i],chi[j])