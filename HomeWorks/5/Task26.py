# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def extent(number: int, degree: int):
    if degree > 0:
        return number * extent(number, degree - 1)
    elif degree < 0:
        return 1 / number * extent(number, degree + 1)
    else:
        return 1


num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))

print(f"Число {num_a} в степени {num_b} равно {extent(num_a, num_b)}")
