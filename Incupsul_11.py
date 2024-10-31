#ИНКАПСУЛЯЦИЯ видео 1
class Test():
    def __init__(self):
        self.public = 'Публичный атрибут'
        self._protected = 'Защищенный атрибут'
        self.__private = 'Приватный атрибут'

    def get_private(self):   #получаем , берем инф-ю из приватного атрибута
        return self.__private  #возвращаем значение, которое лежит в self.__private

    def set_private(self, value):  #с приватными атрибутами мы м. раб. тоько внутри класса, в кот.они
        self.__private = value     #прописаны. Извне мы их брать не может - б. ошибка


test = Test()
print(test.public)  #открытый атрибут печатается обычным образом
print(test._protected) #защищ-й атр, печатается, но так не рекомендуется делать в программе

print(test.get_private()) #я получил значение (возврат ф-ции) и просто его использую

test.set_private('Получили значение приватного атрибута')  #заменяем значение приватного атрибута
print(test.get_private())  #снова использ ф-ю пуе lkz gjkextybz b dsdjlf yjdjuj pyfxtybz fnhb,enf 


