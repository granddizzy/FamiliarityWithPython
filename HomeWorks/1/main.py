#task 2

"""
while (True):
    str = input("Введите трехзначное число: ")

    if not str.isdigit() or len(str) != 3:
        print("Не правильно указано число!!!")
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

"""
while (True):
    str = input("Введите 6 значный номер билета:")

    if not str.isdigit() or len(str) != 6:
        print("Не правильно указан номер!!!")
    else:
        break

num = int(str)

sumLleft = num // 100000 + (num // 10000 - num // 100000 * 10) + (num // 1000 - num // 10000 * 10)
sumRight = num % 10 + (num % 100 // 10) + (num % 1000 // 100)

if sumLleft == sumRight:
    print("Это число СЧАСТЛИВОЕ!!!")
else:
    print("Это не счастливое число.")
"""

#task 8

n = int(input("Введите количество долек с одной стороны n: "))
m = int(input("Введите количество долек с другой стороны m: "))
k = int(input("Введите количество долек которые хотите отломить k: "))

if k >= n * m:
    print("Ешь сразу всю :)")
elif k % m == 0 or k % n == 0:
    print("Все получится!!!")
else:
    print("За один раз отломать столько долек не выйдет :(")