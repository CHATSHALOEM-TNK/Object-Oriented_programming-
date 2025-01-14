class Animal :
    def _init_(self,name,age,color):
        self.name = name 
        self.age = age 
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"
class Dog(Animal):
    def _init_(self,name,age,color,race):
        super().race = race 
    def _showinfo_(self):
        return f'หมาพันธ์ {self .race} มี {super() .showinfo}'


Animal1 = Animal('ปีเตอร์ม',12,"ดำ" )
print(Animal1.showinfo())    