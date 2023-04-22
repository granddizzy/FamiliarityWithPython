# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint as ri

list1 = [ri(1, 5) for _ in range(10)]
print(list1)


def replace1(list1: list) -> None:
    min_rating = min(list1)
    max_rating = max(list1)

    for i in range(len(list1)):
        if list1[i] == max_rating:
            list1[i] = min_rating


def replace2(list1: list) -> list:
    min_rating = min(list1)
    max_rating = max(list1)

    return [min_rating if rating == max_rating else rating for rating in list1]


print(replace2(list1))

replace1(list1)
print(list1)



