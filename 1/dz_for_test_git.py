# # ооп часть 1
#
# # объявление класса
#
# class Cat:
#     #атрибуты класса или константы класса = переменная
#     paws = 4
#     tail = 1
#     mustache = True
#     head = 1
#     #color = 'red'
# # финкция инициализации
#     def __init__(self, color):
#         self.color = color
#
#
#
# # создание объекта (экземпляра класса)
# my_cat1 = Cat() # создаем  объкт класса Cat
# print(type(my_cat1))
# # вывод параметров объекта
# print(f'у моего кота {my_cat1.tail} хвост')
# print(f'у моего кота {my_cat1.color} color')
#
# my_cat2 = Cat('white')
# print(type(my_cat2))
# print(f'у моего второго кота {my_cat2.tail} хвост')
# print(f'у моего второго кота {my_cat2.color} color')
#
# my_cat3 = Cat('black')
# print(f'у моего 3 кота {my_cat3.color} color')

#zad 1
# создать класс Студент у которого специализация "computer science" общая для всех
# а индивидумальные свойства для: возраст и имя

class Student:
    spec = 'computer science'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('создание класса')

    def sleep(self):
        return (f'{self.name} спит на парах')

    def run(self):
        return (f'{self.name} бегает по классу')

    def new_name(self):


student1 = Student('Валера', 25)
print(f'Его зовут - {student1.name}!')
print(student1.sleep())

student2 = Student('Jan Grinchenko', 33)
print(f'Его зовут - {student2.name}!')
print(student2.run())


