import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    return bmi
def danh_gia(bmi):
	if bmi<18.5:
		return 'Bạn đang ở trạng thái Gầy'
	elif 18.5<=bmi<=24.99:
		return 'Bạn đang ở trạng thái Bình thường'
	else:
		return'Bạn đang ở trạng thái Thừa cân'		
can_nang=int(input("Nhập cân nặng (kg): "))
chieu_cao=float(input("Nhập chiều cao (m): "))    
bmi=tinh_bmi(can_nang,chieu_cao)
print("BMI = %0.2f"%bmi)
print(danh_gia(bmi))