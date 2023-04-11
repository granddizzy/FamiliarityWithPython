# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

import random

n = int(input("Введите количество арбузов: "))

max_weight = 0
minWeight = 0
numberMaxWeight = 0
numberMinWeight = 0

for i in range(1, n+1):
    # m = int(input(f"Введите массу арбуза номер {i}: "))

    m = random.randint(1, 30000)

    print(m, end=" ")

    if i == 1:
        minWeight = m
        numberMinWeight = 1

        max_weight = m
        numberMaxWeight = 1
    elif m > max_weight:
        max_weight = m
        numberMaxWeight = i
    elif m < minWeight:
        minWeight = m
        numberMinWeight = i

print(f"Арбуз для себя номер {numberMaxWeight} c массой {max_weight}")
print(f"Арбуз для тещи номер {numberMinWeight} c массой {minWeight}")
