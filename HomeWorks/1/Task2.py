#Задача 2: Найдите сумму цифр трехзначного числа.

while True:
    str = input("Введите трехзначное число: ")

    if not str.isdigit() or len(str) != 3:
        print("Не правильно указано число!!!")
    else:
        break

sumNumbers = int(str[0]) + int(str[1]) + int(str[2])

print(f"Сумма цифр числа {str} равна {sumNumbers} ({int(str[0])} + {int(str[1])} + {int(str[2])})")