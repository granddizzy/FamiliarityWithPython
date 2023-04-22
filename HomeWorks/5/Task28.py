# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def summa(num_a: int, num_b: int) -> int:
    if num_a == 0:
        return num_b
    return summa(num_a - 1, num_b + 1)


number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))

print(summa(number_a, number_b))
