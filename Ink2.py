class Car:
    def __init__(self, make, model):  #ф-ция инициализации(создания), в к-ю б. передаваться атрибуты(хар-ки) производитель и модель
        self.public_make = make  #публич атрибут(хар-ка) - производитель
        self._protected_model = model  #защищенный атрибут - модель
        self.__private_year = 2022  #приватный атрибут - год выпуска
    #методы:
    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."
    def _protected_method(self):
        return "Это защищенный метод."
    def __private_method(self):
        return "Это приватный метод"
class ElectricCar(Car):   #дочерний класс электрокаров на базе род.класса Car
    def __init__(self, make, model, battery_size):  #помимо атрибутов род.класса, вводим дополн-й
        super().__init__(make, model)                #- размер батареи
        self.battery_size = battery_size

    def get_details(self):
        #можно обратиться к откр. и защ. атрибуту, но НЕ к Приватному!
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery_size}"
        #нельзя напрямую обратиться к __private_year и __private_method()
        return details

#создадим экземпляр класса ElectricCar
tesla = ElectricCar('Tesla', 'Model S', 100)

#сейчас попробуем получить доступ к публичному методу и атрибуту
print(tesla.public_make)
print(tesla.public_method())

#доступ к защащ-му атр и методу (не реком-ся, но возможно
print(tesla._protected_model)
print(tesla._protected_method())

#доступ к приватному атр
print(tesla._Car__private_year)









