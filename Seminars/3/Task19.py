# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint

numbers_list_1 = []
for i in range(20):
    numbers_list_1.append(randint(-10, 11))

numbers_list = [randint(-10, 11) for i in range(20)]

print(numbers_list)

shift = int(input("Введите число сдвига: "))

for i in range(shift):
    numbers_list.insert(0, numbers_list.pop())

print(numbers_list)