# Создайте класс Animal с методом make_sound(). Затем создайте несколько дочерних
# классов (например, Dog, Cat, Cow), которые наследуют Animal, но изменяют его поведение
# (метод make_sound()). В конце создайте список содержащий экземпляры этих животных и
# вызовите make_sound() для каждого животного в цикле.

class Animal():  # это базовый класс, поэт. можно не прописывать методы
    def make_sound(self): #от него б. наслед-ся др.классы и уже там пропишем, что б.говорить различные животные
        pass

class Dog(Animal):  # наследуем класс Dog от класса Animal
    def make_sound(self): # переопределяем метод Make_sound -чтобы собака говорила гав
        print("гав")

class Cat(Animal):
    def make_sound(self):
        print("мяу")

class Cow(Animal):
    def make_sound(self):
        print("муу")

animals = [Dog(), Cat(), Cow()] #это будет список экз-ров класса,
for animal in animals:  # перебираем список animals  и каж отдельное животное попадает в перем-ю animal
    animal.make_sound() # вызывается метод класса, соответствующий данному животному



