# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_it_simple_number(number: int) -> bool:
    if number in [1, 2]:
        return True
    for i in range(3, number // 2 + 1, 2):
        if not number % i:
            return False
    return True


input_number = int(input("Введите число: "))
print("Да" if is_it_simple_number(input_number) else "Нет")
