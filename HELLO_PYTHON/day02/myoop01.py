class Animal:
    def __init__(self):
        self.age = 1
        
    def happyBirthday(self):
        self.age += 1
        
class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.money = 10000
        
    def albamon(self):
        self.money += 1
        
h = Human()

print(h.age)
h.happyBirthday()
h.happyBirthday()
h.happyBirthday()
h.happyBirthday()
print(h.age)
    
    


        

