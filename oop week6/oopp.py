class   Cat :
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ 
        self.age = อายุ
        self.color = สี 
        self.hungry =  ความหิว
    def eat(self,อาหาร):
        self.hungry+=อาหาร
cat1=Cat(ชื่อ="ศรีเงิน",อายุ = 10,สี = "ส้ม",ความหิว=5)
cat2=Cat("ศรีทอง",8,"ดำ",ความหิว=5)
print(cat1.color)
print(cat2.age)