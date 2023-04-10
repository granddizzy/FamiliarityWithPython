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

n = int(input("Введите количество арбузов: "))

maxWeight = 0
minWeight = 0
numberMaxWeight = 0
numberMinWeight = 0

for i in range(1, n+1):
    m = int(input(f"Введите массу арбуза номер {i}: "))

    if i == 1:
        minWeight = m
        numberMinWeight = 1

        maxWeight = m
        numberMaxWeight = 1
    elif m > maxWeight:
        maxWeight = m
        numberMaxWeight = i
    elif m < minWeight:
        minWeight = m
        numberMinWeight = i

print(f"Арбуз для себя номер {numberMaxWeight} c массой {maxWeight}")
print(f"Арбуз для тещи номер {numberMinWeight} c массой {minWeight}")
