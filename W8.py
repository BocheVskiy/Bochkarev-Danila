request = input("Чётные или нечётные?\n").lower()

if request == "четные" or request == "чётные" :
    for i in range(21):
        if i % 2 == 0:
            print(i, end=" ")
elif request == "нечетные" or request == "нечётные":
    for i in range(21):
        if i % 2 != 0:
            print(i, end=" ")
else:
    print("Я не понимаю, что вы от меня хотите...")