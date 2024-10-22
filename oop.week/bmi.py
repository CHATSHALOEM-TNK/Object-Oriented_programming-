name = input("กรุณาป้อนชื่อจริง: ")
print(name)
student_id = input("กรุณาป้อนรหัสประจำตัวนักศึกษา: ")
print(student_id)
year = input("กรุณาป้อนชั้นปี: ")
print(year)
nickname = input("กรุณาป้อนชื่อเล่น: ")
print(nickname)


height = float(input("กรุณาป้อนส่วนสูง (เมตร): "))
print(height)
weight = float(input("กรุณาป้อนน้ำหนัก (กิโลกรัม): "))
print(weight)
total = height + weight

print("ชื่อ" + name + "รหัส" + student_id + "ชั้นปี" + year + "ชื่อเล่น" + nickname + "สูง"  + str (height) + "น้ำหนัก" + str (weight) )