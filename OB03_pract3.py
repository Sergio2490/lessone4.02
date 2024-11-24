#Задача №3.
#Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения
# автора в качестве объекта.

class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title  # б.передаваться как аргумент = это хар-ка класса Book
     # а сейчас, с пом. Агрегации, мы м.передать сюда, в наш класс - автора. Сначала создадим ниже объект класса Книга
        self.author = author

    def get_info_book(self):
        print(f"{self.title} - {self.author.name}")  #из класса Book обращаемся к хар-ке класса Author,
                   #тк мы передали сюда, в класс Book объект класса Авток как хар-ку

author = Author("Лев Толстой", "русский")  # сначала созд объект класса Автор
# а теперь надо добавить его, как объект, в класс Кинига
book = Book("Война и мир", author)  #мы передаем автора,он сохраняется как аргумент author
          #  в класс Book. И записываем в классе Book: self.author = author

print(author.name) #здесь мы так же, как и ф ф-ции клBook, м. исп-ть автора

book.get_info_book()  #пробуем исп-ть эту ф-цию




