# _*_coding:cp1251_*_
from datetime import date
def Let():

    print("������� ����, ����� � ��� ������ ��������!")

    today = date.today()
    try:
        day = int(input("������� ����:""- "))
        if 1<=day<=31:
            pass
        else:
            print("������� ����� �� 1 �� 31!")
    except (ValueError, (NameError)):
        print("������������ �������� ���!")
    try:
        month = int(input("������� �����:""- "))
        if 1<=month<=12:
            pass
        else:
            print("������� ����� �� 1 �� 12!")
    except (ValueError, (NameError)):
        print("������������ �������� ������!")
    try:
        year = int(input("������� ���:""- "))
        if 1000<=year<today.year:
            pass
        else:
            print("������� ��������� ���!")
    except (ValueError, (NameError)):
        print("������������ �������� ����!")
    try:
        age = today.year - year - ((today.month, today.day) < (month, day))
        last_dig = age % 10
        if 10 < age < 20:
            print("���", age, "���!")
        elif 1 < last_dig < 5:
            print("���", age, "����!")
        elif last_dig == 1:
            print("���", age, "���!")
        else:
            print("���", age, "���!")
    except NameError:
        print("�� ����� �� ������ ������!!!")
