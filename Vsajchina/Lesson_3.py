# _*_coding:cp1251_*_
from math import sqrt, pi
print('�������� ��������\n�� ���������� �������:''\n                      ����������� - "K"'
      '\n                      ������� ����� - "R"''\n                      ������� �������������� - "P"'
      '\n                      ������� ������������ - "T"')
comanda = input("������� �������: ")
def summ(a, b):  # ������� ��������
    return a + b  # ����� ����������
def vysh(a, b):  # ������� ���������
    return a - b  # ����� ����������
def pro(a, b):  # ������� ��������
    return a * b  # ����� ����������
def raz(a, b):  # ������� ��������
    return a / b  # ����� ����������
def plosh_kruga(r):
    return pi * r ** 2
def plosh_prjamoug(S):
    return j * i
def treugolnik(T):
    return sqrt(p * (p - a) * (p - b) * (p - c))
if comanda == "K":
    print("**********************************************************************************************************")
    print("     �����������     "*5)
    print("**********************************************************************************************************")
    while True:  # ����������� ���� �����������
        a = float(input("������� ����� 1: "))  # ������������ ������ ����� 1
        b = float(input("������� ����� 2: "))  # ������������ ������ ����� 2
        c = input("������� ��������: ")  # ������������ ������ �������� ( +, -, *, / )
        # ��� ������ �� ������������ ������� "s"
        if c == "+":
            print("���������: ", summ(a, b))
        elif c == "-":
            print("���������: ", vysh(a, b))
        elif c == "*":
            print("���������: ", pro(a, b))
        elif c == "/":
            print("���������: ", raz(a, b))
        elif c == "s":
            break
elif comanda == "R":
    r = float(input("������� ������ ����� R= "))
    print("������ �����:")
    print("             R = ", plosh_kruga(r))
elif comanda == "P":
    print("������� ��������������:")
    j = float(input("������� ������� a: "))
    i = float(input("������� ������� b: "))
    print("������� ��������������:")
    print("                       S =", plosh_prjamoug(j * i))
elif comanda == "T":
    print("������� ������� ������������:")
    a = float(input('������� ������� a: '))
    b = float(input('������� ������� b: '))
    c = float(input('������� ������� c: '))
    p = (a + b + c) / 2
    print("������� ������������:")
    print("                     S =", treugolnik(sqrt(p * (p - a) * (p - b) * (p - c))))