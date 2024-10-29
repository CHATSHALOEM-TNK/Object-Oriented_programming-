i = 0 
while True :
    num = int(input("ใส่ค่า : "))
    if num > 0 :
        i +=  num
        print(f"ผลรวมกันตอนนี้ {i}")
    elif num == 0 : 
        print(f"ผลรวมกันตรงนี้ {i}")
        print(f"ผลรวมทั้งหมด{i}")
        break 