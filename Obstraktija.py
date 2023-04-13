# _*_coding:cp1251_*_
from abc import abstractmethod
class Transport:
    def __init__(self):
        pass
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass
# ����� �������
class Plane(Transport):
    def __init__(self):
        pass
    def run(self):
        print("������� �����")
    def on(self):
        print("������� �������")
    def off(self):
        print("������� ��������")

    def vzlet(self):
        print("������� ��������")
    def pos(self):
        print("������� �������")
# ����� ����������
class Car(Transport):
    def __init__(self):
        pass
    def run(self):
        print("���������� ����")
    def on(self):
        print("���������� �������")
    def off(self):
        print("���������� ��������")
    def vzlet(self):
        print("���������� ����")
    def pos(self):
        print("���������� �����������")
# ����� ��������
class Animal():
    def __init__(self):
        pass
    def run(self):
        print("�������� ������")
    def on(self):
        print("�������� ����������")
    def off(self):
        print("�������� ����")
    def pos(self):
        print("�������� �����")
# �������� ��������
plane1 = Plane()
plane1.on()
plane1.vzlet()
plane1.run()
plane1.pos()
plane1.off()
print("****************************************************************************************************")
# �������� ����������
car1 = Car()
car1.on()
car1.run()
car1.pos()
car1.off()
print("****************************************************************************************************")
# �������� ���������
aanimal1 = Animal()
aanimal1.on()
aanimal1.run()
aanimal1.pos()
aanimal1.off()