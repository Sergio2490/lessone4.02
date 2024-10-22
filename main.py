#OB02 Наследование
class Bird:  # БАЗОВЫЙ, Родительский класс
    def __init__(self, name, voice, color):
        self.name = name   #свойства, характеристики птицы
        self.voice = voice
        self.color = color
    def fly(self):
        print(f'{self.name} летает')
    def eat(self):
        print(f'{self.name} кушает')
    def sign(self):
        print(f'{self.name} поет - {self.voice}')
    def info(self):    #вывод всей инф-ции о птице
        print(f'{self.name} - имя')
        print(f'{self.voice} - голос')
        print(f'{self.color} - окрас птицы')

class Pigeon(Bird):  #Дочерний класс Голубь, наследуется от базового класса Bird
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color) #чт.забрать хар-ки из.род-го класса Bird и дописать свои-
                       #надо использовать метод super(). Это обеспечит доступ к методам род-го
                       #класса без явного указания = делает код универсальным. И также, super позвол.
                       #избежать проблем с множеств-м наслед-ем(класс наслед-ся от неск. родителей)
        self.favorite_food = favorite_food  # вводим нов атрибут класса Голубь - любимая еда
    def walk(self):  #кроме своей хар-ки Люб.еда, вводим тажкже свой метод Гулять
        print(f'{self.name} гуляет')

#Создаем объект класса голубь
bird1 = Pigeon('Гоша', 'курлык', 'серый', 'хлебные крошки')  #Вводим хар-ки, тк унаследовали это от родит-го класса Bird
bird1.sign()
bird1.info()
bird1.walk()
