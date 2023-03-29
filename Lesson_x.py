from random import randint

jornal = "spisok.txt"   # имя файла
sp = []

for i in range(5):
    sp0 = input("Введите строку: ")
    sp.append(sp0 + " оценка - ")
    sp1 = input("Введите оценку:")
    sp.append(sp1 + "\n")
print(sp)
with open(jornal, "w") as file:
    for i in sp:
        file.write(i)
with open(jornal, "r") as file: # Считываем файл
    mark_count = 0
    mark_sum = 0
    print("Ученики чьи оценки меньше 3-х:")
    for i in file.readlines():  # перебор учеников из файла
        i = i.rstrip("\n")      # удаление сомволов в конце строки
        mark_count += 1         # количество (учеников) оценок
        mark = int(i[-1])       # получаем оценки и переводим в числа
        mark_sum += mark        # суммируем оценки
        if mark < 3:
            print("                             ", *i[:-1].split(" - "))
    # print(i)  # вывод списка учеников из файла
    print("************************************************************")
    print("Средний бал по классу:", mark_sum / mark_count)
    print("Количество учеников\nв классе:", mark_count)