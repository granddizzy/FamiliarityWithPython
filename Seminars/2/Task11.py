# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

a = int(input("Введите число: "))

pos = -1

if a == 0:
    pos = 1
elif a == 1:
    pos = 2
else:
    currentNumber = 1
    previousNumber = 1
    pos = 3

    while a >= currentNumber:
        nextNumber = currentNumber + previousNumber

        pos += 1

        if nextNumber == a:
            break

        previousNumber = currentNumber
        currentNumber = nextNumber
    else:
        pos = -1

print(f"Позиция этого числа в последовательности Фибоначчи {pos}")