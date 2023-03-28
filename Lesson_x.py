
# with open("jornal.txt",  "w") as file:
#     file.write("Шилов Роман Георгиевич - 5\n"
#                 "Иванов Евгений Егоревич - 3\n"
#                 "Скрябин Станислав Александрович - 4\n"
#                 "Арнаутов Павел Николаевич - 2\n"
#                 "Шамангалиев Айдар Джавдетович - 2\n"
#                )

with open("jornal.txt") as file:
    # text = file
    for i in file:
        print(i, end="")