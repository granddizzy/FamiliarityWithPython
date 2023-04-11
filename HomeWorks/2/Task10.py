# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

from random import randint

n = int(input("Введите количество монеток n: "))

coins = [randint(0, 1) for i in range(n)]

print(coins)

print(f"Минимальное количество монеток которое нужно перевернуть {coins.count(0) if coins.count(0) <= coins.count(1) else coins.count(1)}")

# через циклы
count_up = 0
count_down = 0
for i in coins:
    if i == 0:
        count_up += 1
    else:
        count_down += 1

if count_up > count_down:
    max_count = count_down
else:
    max_count = count_up

print(f"Минимальное количество монеток которое нужно перевернуть {max_count}")

