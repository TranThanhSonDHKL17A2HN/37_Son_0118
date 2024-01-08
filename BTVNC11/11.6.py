chieu_cao=[74,74,72,72,73,69,69,71,76,71]
def doi(x):
    return x*0.0254
ccmoi = [doi(x) for x in chieu_cao]
print('Đổi inch sang m:',ccmoi)
print('In 3 chiều cao đầu tiên:',ccmoi[0:3])
print('In 3 chiều cao cuối cùng:',ccmoi[-3:])
print("Chiều cao max:",max(ccmoi))
print("Chiều cao min:",min(ccmoi))
print("Chiều cao trung bình:",sum(ccmoi)/len(ccmoi))
ccmoi.sort()
print('Chiều cao tăng dần:',ccmoi)
ccmoi.sort()
ccmoi.reverse()
print('Chiều cao giảm dần:',ccmoi)