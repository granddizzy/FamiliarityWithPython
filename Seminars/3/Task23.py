# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

input_list = [randint(-10, 11) for i in range(5)]

print(input_list)

count = 0
for i in range(1, len(input_list)):
    if int(input_list[i]) > int(input_list[i - 1]):
        count +=1

print(count)

print(len([input_list[i] for i in range(1, len(input_list)) if int(input_list[i]) > int(input_list[i - 1])]))

