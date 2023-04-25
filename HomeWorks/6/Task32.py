# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint as ri

size1 = ri(1, 10)
list1 = [ri(0, 10) for _ in range(size1)]
print(list1)

max_ = 3
min_ = 1

list2 = [i[0] for i in enumerate(list1) if max_ >= i[1] >= min_]
print(list2)
