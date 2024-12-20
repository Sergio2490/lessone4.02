#Домашнее задание OB03
#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

#Дополнительно: Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name   # привязываем хар-ки к нашему классу
        self.age = age

    def make_sound(self):
        pass
    def est(self):
        print(f'{self.name} кушает')

class Bird(Animal):
    def make_sound(self):  # переопредели ф-ю make_sound
        print('чирик чирик')

class Mammal(Animal):  # млекопитающие
    def make_sound(self):
        print('мяу')
class Reptile(Animal):
    def make_sound(self):
        print('шшшшшш')

# п.3 Полиморфизм
def animal_sound(animals): # Переопределяем метод make_sound для конкретного животного
    for animal in animals:
        animal.make_sound()  # для каж конкретного жив-го в списке б. выз метода make_sound

# п. 4 Композиция
class Zoo():
    def __init__(self):
        self.animals = []  # 2 списка, куда б. доб всех наших животный
        self.staff = []     # и всех сотрудников

    def add_animal(self, animal):  # сейчас сделаем метод для добавления животных в Зоопарк (в список)
        self.animals.append(animal)  # ф-я б. доб. именно в наш список (self.animals) конкретное животное
        print(f'Животное {animal.name} добавлено в список')  # Животное добавлено в Зоопарк
    def add_staff(self, new_staff):  # сейчас сделаем метод для добавления сотр-ков в Зоопарк (в список)
        self.staff.append(new_staff)  # ф-я б. доб. именно в наш список (self.staff) конкретного сотрудника
        print(f'Сотрудник {new_staff} добавлен в список')  # Сотрудник добавлен в Зоопарк

# п.5
class ZooKeeper():
    def feed_animal(self, animal):  # передаем в аргументе животное, которое сотр б. кормить
        print(f'Сотрудник кормит {animal.name}')  #указываем конкретное назв животного

class Veterinarian():
    def heal_animal(self, animal):
        print(f'Ветеринар лечит {animal.name}')

# Сейчас создадим обюъекты классов gj ;bdjnysv
bird1 = Bird('Скворец', 1)
mammal1 = Mammal('Котенок', 2)
reptile1 = Reptile('Змея', 3)

# Создадим объекты, связанные с зоопарком
zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

# Добавим в зоопарк новых животных
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

# Добавим в зоопарк новых сотрудников
zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

# Используем и другие ф-ции - animal_sound(animals). Сюда надо передавать список животных
# и ф-ция б. переопределять их голоса. (animals) - это атрибут(хар-ка) класса Zoo, поэтому
# мы б. указывать zoo.animals, чт. добраться(передать) до списка животных
animal_sound(zoo.animals)

keeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)