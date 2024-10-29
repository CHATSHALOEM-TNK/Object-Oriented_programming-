import random
print("โปรแกรมเป่ายิ้งฉุบ")
while True:
    a = random.choice(["ค้อน","กรรไกร","กรรไกร"])
    print(f"{a}")
    print("ค้อน","กรรไกร","กรรไกร")
    value = str(input('คุณเลือก'))
    if (a == value ):
        print("ผลลัพท์เสมอ ")
        print("-------------------")
    elif (value == 'ค้อน' and a== "กรรไกร"):
        print("ผลลัพท์คือเสมอ")
        print("--------------------")
    elif (value == 'กระดาษ' and a== "ค้อน"):
        print("ผลลัพท์คือชนะ")
        print("--------------------")
    elif (value == 'กรรไกร' and a== "กระดาษ"):
        print("ผลลัพท์คือชนะ")
        print("--------------------")
    else:
        print('ผลลัพท์ คือ แพ้')
        print("------------------------")