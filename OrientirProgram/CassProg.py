# _*_coding:cp1251_*_

class Person():
    '''������ �������'''
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car
    def hello(self):
        print("���:       ", self.name, "\n�������:   ", str(self.age), "���.", "\n���������\n����������:",  self.car)

info = Person("�������", 38, "Lada")
info.hello()

print(info.car)
print(info.name)
print(info.age)