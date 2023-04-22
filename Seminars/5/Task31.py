# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


def find_fibonnachi(pos: int) -> int:
    if pos == 1 or pos == 2:
        return 1

    return find_fibonnachi(pos - 1) + find_fibonnachi(pos - 2)


pos = int(input("Введите номер числа: "))
print(find_fibonnachi(pos))

