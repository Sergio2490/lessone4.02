# Пример Агрегации
class Teacher():
    def teach(self):
        print('Преподаватель учит')

class School():   # Пропишем в def__init, что мы передаем нашего преп-ля в школу
    def __init__(self, new_teacher): #через эту перем-ю (new_teacher) в этот класс б. передаваться инф-я об объекте класса
        self.teacher = new_teacher  #создаем новую хар=-ку и сохр в нее нашего препод-ля, которого передали

    def start_lessone(self):  # будем начинать урок
        self.teacher.teach()  # получаем доступ к ф-ции teach( другого класса Teacher

my_teacher = Teacher()
my_school = School(my_teacher)
my_school.start_lessone()