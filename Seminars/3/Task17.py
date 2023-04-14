# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint

numbers_list_1 = []

for i in range(20):
    numbers_list_1.append(randint(-10, 11))

print("Количество не повторяющийхся элементов равно", len(set(numbers_list_1)))





numbers_list = [randint(-10, 11) for i in range(20)]

print(numbers_list)
print("Количество не повторяющийхся элементов равно", len(set(numbers_list)))