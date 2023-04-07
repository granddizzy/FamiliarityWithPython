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