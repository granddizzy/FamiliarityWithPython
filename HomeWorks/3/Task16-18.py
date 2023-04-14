# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
#
# 5
# 1 2 3 4 5
# 3
# -> 1


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
#
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

input_list = [randint(0, 10) for _ in range(1, 10)]

print(input_list)

num = int(input("Введите число: "))

count = input_list.count(num)

if not count:
    min_distance = 0

    for number in set(input_list):
        distance = abs(number - num)

        if not min_distance or distance < min_distance:
            nearest = [number]
            min_distance = distance
        elif distance == min_distance:
            nearest.append(number)

    if len(nearest) == 1:
        print(f"Ближайшее число {nearest[0]}")
    else:
        print(f"Ближайшие числа {nearest}")
else:
    print(f"Число встречается {count} раз")



