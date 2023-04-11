# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

import random

days = int(input("ведите количество рассматриваемых дней 1 ≤ N ≤ 100: "))

max_thaw_durations_days = 0
current_thaw_durations_days = 0
average_daily_temperature = 0

for i in range(1, days+1):
    # averageDailyTemperature = int(input(f"Введите среднесуточную температуру в день номер {i}: "))

    average_daily_temperature += random.randint(-3, 3)

    print(average_daily_temperature, end=" ")

    if average_daily_temperature > 0:
        current_thaw_durations_days += 1
    else:
        current_thaw_durations_days = 0

    if current_thaw_durations_days > max_thaw_durations_days:
        max_thaw_durations_days = current_thaw_durations_days

print(f"\nДлительность максимальной оттепели за данный период составляет {max_thaw_durations_days} дней")