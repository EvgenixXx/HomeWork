filename = "belka.txt"
with open(filename) as file:
    text = file.read()
    print(text)
    print("*************************************************")
    text1 = text.split()
    print(text1)
    print(text1[:3], [4])

    while True:
        sp_list = []
        if i == text1[:3][4]:
            sp_list.append(i)
        print(sp_list)