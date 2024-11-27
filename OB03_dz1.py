#Домашнее задание OB03

class Animal():
    def __init__(self, name, age):
        self.name = name   # привязываем хар-ки к нашему классу
        self.age = age

    def make_sound(self):
        pass
    def est(self):
        print(f'{self.name} кушает')

class Bird(Animal):
    
