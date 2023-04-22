# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_print(input_str: str, pos: int) -> None:
    print(input_str[pos - 1], end="")
    if pos != 1:
        reverse_print(input_str, pos - 1)


input_str = input("Введите строку: ")
size = len(input_str)

reverse_print(input_str, size)
