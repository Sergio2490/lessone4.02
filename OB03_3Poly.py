# Полиморфизм
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):  # ф-ция вне классов. В эту ф-цию б.передаваться объект класса (dog или cat)
    print(animal.speak())  # И для любого животного мы м. вызвать ф-цию speak()

dog = Dog()
cat = Cat()

animal_speak(dog) #в ф-ю передаем значение атрибута (объект класса dog)
animal_speak(cat)

