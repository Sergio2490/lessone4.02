#Разбор дз OB02 - классы User и Admin

class User():
    def __init__(self, user_id, name): #уровень доступа user б считаться базовой хар-кой, поэтому
        self.name = name          # при создании экземпляыра класса указывать его не требуется
        self._user_id = user_id   #указываем хар-ки класса
        self._name = name
        self._level = "user"

    def get_user_id(self):
        return self._user_id
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def set_name(self, name): #сетер для смены имени пользователя
        self._name = name

class Admin(User):
    def _init__(self, user_id, name):
        super().__init__(user_id, name) #с пом. метода super() мы всё инициализируемпередаем
                                        #из родит-го класса User - параметры родительского класса
        self._level = "admin"  # задаем нов уровень доступа. А тк мы использовали метод super(, то
                            # хар-ки self._user_id и self._name - берутся из род-го класса, а мы
                            # лишь заменяем уровень доступа
    def add_user(self, user_list, user): #новый метод? user_list - список всех пользователей
        user_list.append(user)  #доб в список user_list польз-ля user
        print(f"Пользователь {user.get_name()} успешно добавлен в список")
        print(user_list)  #печ плохо - [<__main__.User object at 0x000001DF5A12E6C0>]
    def remove_user(self, user_list, user):
        user_list.remove(user)   #удал конкретного пользователя

users = []  #создадим пустой список для хранения польз-лей, к-х мы б. добавлять
admin = Admin("a1", "Gosha")  # создадим объект класса Admin
user1 = User("u1", "Stepa")

#Используем методы (прочитаем информацию)
print(user1.get_name())

#сейчас добавим польз-ля в наш список - делаем это через админа
admin.add_user(users, user1)





