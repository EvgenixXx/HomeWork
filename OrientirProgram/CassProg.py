# _*_coding:cp1251_*_
class Animal():  # ������������ (�������) �����
    def __init__(self, breed,  name, sex):  # ���� ��������� ������
        # ������������ ��������
        self.breed = breed      # ������
        self.name = name        # ���
        self.sex = sex          # ���
        # ����������� ��������
        self.age = 3.5          # �������
        # ������
        self.skills = "���� �� �����, ����������� ���������� � ������������� �������"
    def info_Animal(self):     # ����� 1 "���������� � ��������" � ����� � �������
        print("������ ���������:  ", self.breed, "\n��� ���������:     ", self.name, "\n��� ���������:     ", self.sex)
    def age_Animal(self):   # ����� 2 "������� ���������" � ����� � �������
        print("������� ���������: ", str(self.age), "���/����")
    def skiils_Animal(self):   # ����������� � ������ � ����� � �������
        print("����������� � ������:", "\n                     " + self.skills + ".")
    def locotion_Animal(self):
        print("���������������:", "\n                " + self.name, "���������� �� ������.")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# ������� ������ � 1. ���� ��������� ����������
Animal_1 = Animal("�������", "����", "�������")
# ������� ������ � 2. ���� ��������� ����������
Animal_2 = Animal("�������", "���", "�������")
print("*******************************************************************")
# # ����� ������ ������
# Animal_1.info_Animal()
# Animal_1.age_Animal()
# Animal_1.skiils_Animal()
# Animal_1.locotion_Animal()
# # ����� ������ ������
# Animal_2.info_Animal()
# Animal_2.age_Animal()
# Animal_2.skiils_Animal()
# Animal_2.locotion_Animal()
class Dog(Animal):  # ������������ ������ (����� ���������)
    def __init__(self, breed, name, sex):   # ������� ���������
        super().__init__(self, name, sex)   # ����� ���� �� ������������� ������
        self.age = 1                        # ���� ��������� ������
        self.name = name                    # ���� ��������� ������
        self.breed = breed                  # ���� ��������� ������
    def location(self):
        print("���������������:", "\n                " + self.name, "���������� �� �����������.")

# ������� ������ � 1. ���� ��������� ����������
Dogs = Dog("�������", "�����", "�������")

# ������� ������ � 2. ���� ��������� ���������� ������� � 1 �� ������������� ������
Dogs_2 = Animal("���-���", "������", "�������")
# ����� ������ ������
# Dogs.info_Animal()
# Dogs.age_Animal()
# Dogs.location()
# Dogs_2.locotion_Animal()