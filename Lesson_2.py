# _*_coding:cp1251_*_
with open("lesson_2.txt", "r") as f:
    sp = f.readlines()
    for i in sp:
        print(i, end="")
    print("\n""*****************************************")
    print("���������� ��������\n� ������ ������:")
    lines = 0
    words = 0
    for i in sp:
        lines += 1
        s = i.split()
        print("                - ", (len(i.rstrip("\n"))))
        for j in s:
            words += 1
    print("*****************************************")
    print("���������� �����: ", lines)
    print("���������� ����: ", words)
