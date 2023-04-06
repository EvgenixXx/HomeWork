# _*_coding:cp1251_*_

# ������ �������
import turtle
# �������� ��������
turtle.speed(2)
def move(a): # ������� "move" - ��������
    # �������� (������ - forward, ����� - backward) �������� � ������� ��� (���������� ��������)
    turtle.forward(100)
    # ������� �� (���� - left, ����� - right) �������� � ������� ��� (������ ��������)
    turtle.left(90)
def drawSquare(a):                  # ����� ������� ��������� ��������
    for i in range(4):              # �������� ������� ��������� ��������
        move(a)                     # ����� ������� "move"

def drawSquareColor(a, color):      # ����� ������� ��������� ��������
    # turtle.color(color)             # ��������� � ��������� ����
    # turtle.begin_fill()             # ������ ������������
    for i in range(4):              # �������� ������� ��������� ��������
        move(a)                     # ����� ������� "move"
    # turtle.end_fill()               # ����� ������������

def move2(b):                       # ������� "move" - ��������
    turtle.backward(100)
    # ������� �� (���� - left, ����� - right) �������� � ������� ��� (������ ��������)
    turtle.right(-90)
def drawSquare2(b):                 # ������� ��������� �������� 2
    for i in range(4):              # �������� ������� ��������� ��������
        move2(b)                    # ����� ������� "move"

def drawSquare2Color(b, color):     # ������� ��������� �������� 2
    # turtle.color(color)  # ��������� � ��������� ����
    # turtle.color(color)             # ��������� � ��������� ����
    # turtle.begin_fill()
    for i in range(4):              # �������� ������� ��������� ��������
        move2(b)                    # ����� ������� "move"
    # turtle.end_fill()               # ����� ������������

# ����� ������� ��������� ��������
drawSquareColor(60, 'red'):
# �������� � ������ �� ��� X, Y + ��� - , �������� � ������� ��� (���������)
turtle.goto(-150, -150)
# ����� ������� ��������� �������� 2
drawSquare2Color(160, 'green'):

