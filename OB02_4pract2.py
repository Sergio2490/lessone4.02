# Задача 2. Полиморфизм
# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические
# формы, и метод для расчёта площади каждой формы.
# 1. Создать базовый класс Shape с методом area(), который просто возвращает 0.
# 2. Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square),
#   каждый из которых переопределяет метод area().
# 3. В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# 4. Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape():
    def area(self):
        return 0

class Circle(Shape):  # чт. рассч. S круга, мы д.знать радиус. Поэт, создадим метод init и передадим
    # радиус в него через перем-ю
    def __init__(self, radius):  # при создании объекта класса Circle мы б. передавать радиус через переменную в метод
        self.radius = radius  # привязываем радиус к классу

    def area(self):  # нужно переопределить метод базового класса
        return 3.14 * self.radius **2   # S = pi * r^2

class Rectangle(Shape):
    def __init(self, width, height):  # тоже нужна ф-ция init, тк надо передавать ширину и высоту
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width **2





