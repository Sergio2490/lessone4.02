#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
#2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__level = "user"
    def get_id(self):
       return self.__id
    def get_name(self):
        return self.__name
    def get_level(self):
        return self.__level
    def set_name(self, user, name):
        self.__name = name
        print(f"Имя пользователя {user} изменено на {name}")
    def set_level(self, level):
        self.__level = level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__level = "admin"

    def add_user(self, user):
        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен в список пользователей")

    def remove_user(self, user):
        user_list.remove(user)
        print(f"Пользователь {user.get_name()} удален из списка пользователей")

user_list = []
admin = Admin(1, "admin")

user1 = User(1, "Sergio")
user2 = User(2, "Emilie")

admin.add_user(user1)
admin.add_user(user2)
admin.remove_user(user2)
user1.set_name(user1.get_name(),"Sergy")