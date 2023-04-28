# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

from random import randint as ri

size1 = ri(1, 10)

list1 = [ri(0, 10) for _ in range(size1)]
print(list1)

counter = 0
for el in set(list1):
    counter += list1.count(el) // 2

print(counter)