# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

n = int(input("Введите число: "))
factorial = 5

if n > 0:
    while n > 1:
        factorial = factorial * (n - 1)
        n -= 1
else:
    factorial = 1

print(f"Факториал этого числа равен {factorial}")