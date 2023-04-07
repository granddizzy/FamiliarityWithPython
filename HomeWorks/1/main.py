#task 2

"""
while (True):
    str = input("Введите трехзначное число: ")

    if len(str) > 3 or len(str) < 3:
        print ("Число не трехзначное!!!")
    else:
        break

sumNumbers = int(str[0]) + int(str[1]) + int(str[2])

print(f"Сумма цифр числа {str} равна {sumNumbers} ({int(str[0])} + {int(str[1])} + {int(str[2])})")
"""

#task 4

"""
s = int(input("Введите общее число журавликов: "))

# petr = x
# serg = x
# kate = 2*(x+x) = 4*x
# s = petr + serg + kate = 6*x

if s % 6 != 0:
    print("Такое число журавливков согласно условию сделать бы не смогли!!!")
else:
    x = int(s / 6)

    print (f"Петя сделал: {x}")
    print (f"Сережа сделал: {x}")
    print (f"Катя сделала: {4*x}")
"""

# task 6

while (True):
    num = int(input("Введите 6 значный номер билета:"))

    if num < 0 or num > 999999 or num < 100000:
        print("Не правильно указан номер!!!")
    else:
        break

sumLleft = num // 100000 + (num // 10000 - num // 100000 * 10) + (num // 1000 - num // 10000 * 10)
sumRight = num % 10 + (num % 100 // 10) + (num % 1000 // 100)

if sumLleft == sumRight:
    print("Это число СЧАСТЛИВОЕ!!!")
else:
    print("Это не счастливое число.")