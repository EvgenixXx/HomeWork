# _*_coding:cp1251_*_
x = input("������� ���: ")
def upperfunc(func):
    def wrapper():
        print("������", x.upper()+"!")
    return wrapper
@upperfunc
def hello():
    print("������!",x)
hello()
