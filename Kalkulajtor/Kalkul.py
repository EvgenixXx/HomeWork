# _*_coding:cp1251_*_
from DZ.Raschet import kalkulajtor
from DZ.Geometrija import geometrija
print('�������� ��������\n�� ���������� �������:''\n                      ����������� - "K"'
      '\n                      ��������� - "G"')
comanda = input("������� �������: ")
if comanda == "K":
      kalkulajtor()
elif comanda == "G":
      geometrija()