# _*_coding:cp1251_*_
from math import sqrt, pi
def geometrija():
    def plosh_kruga(r):
        return pi * r ** 2
    def plosh_prjamoug(S):
        return j * i
    def treugolnik(T):
        return sqrt(p * (p - a) * (p - b) * (p - c))
    print("**********************************************************************************************************")
    print("     ���������     " * 5)
    print("**********************************************************************************************************")
    print('�������� ��������\n�� ���������� �������:''\n                      ������� ����� - "R"''\n                      ������� �������������� - "P"'
        '\n                      ������� ������������ - "T"')
    comanda2 = input("������� �������: ")

    if comanda2 == "R":
        r = float(input("������� ������ ����� R= "))
        print("������ �����:")
        print("             R = ", plosh_kruga(r))
    elif comanda2 == "P":
        print("������� ��������������:")
        j = float(input("������� ������� a: "))
        i = float(input("������� ������� b: "))
        print("������� ��������������:")
        print("                       S =", plosh_prjamoug(j * i))
    elif comanda2 == "T":
        print("������� ������� ������������:")
        a = float(input('������� ������� a: '))
        b = float(input('������� ������� b: '))
        c = float(input('������� ������� c: '))
        p = (a + b + c) / 2
        print("������� ������������:")
        print("                     S =", treugolnik(sqrt(p * (p - a) * (p - b) * (p - c))))