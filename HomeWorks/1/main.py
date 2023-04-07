#task 2

while (True):
    str = input("Введите трехзначное число: ")

    if len(str) > 3 or len(str) < 3:
        print ("Число не трехзначное!!!")
    else:
        break

sumNumbers = int(str[0]) + int(str[1]) + int(str[2])

print(f"Сумма цифр числа {str} равна {sumNumbers} ({int(str[0])} + {int(str[1])} + {int(str[2])})")


