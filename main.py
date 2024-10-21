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
    pass

#Создаем объект класса голубь
bird1 = Pigeon('Гоша', 'курлык', 'серый')  #Вводим хар-ки, тк унаследовали это от родит-го класса Bird
bird1.sign()
bird1.info()
