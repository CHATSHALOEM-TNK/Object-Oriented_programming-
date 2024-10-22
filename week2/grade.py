print('โปรแกรมตัดเกรด')
score = int(input('กรอกคะแนนของคุณๅ'))
if score < 0 or score > 100: 
    print('ไม่ให้น้อยกว่า0 และมากกว่า 100 ')
elif score >= 70: 
    print('คุณได้เกรด3 ') 
elif score >= 60: 
    print (' คุณได้เกรด2 ')
elif score >= 50 :
    print ('คุณได้เกรด1 ') 
else:
    print('คุณได้ทำการสอบตก ได้เกรด0 ')
    print('ต้องการแก้หรือไม่ ถ้าต้องการ กด 1 ถ้าไม่ต้องการ กด 2 ')
    c = int(input('กรอกตัวเลือก : '))
    if c == 1: 
        score1 = 50 - score 
        print(f'คุณขาดคะแนนอีก {score}')
    elif c == 2:
        print('สอบตกเหมือนเดิม')
    else: 
        print('กรุณาเลือก 1 และ 2 ')  