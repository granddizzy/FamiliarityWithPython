# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
import random
from math import pi


def find_farthest_orbit(list_of_orbits: list) -> dict:
    dict_ = {round(pi * orbit[0] / 2 * orbit[1] / 2, 2): orbit for orbit in
             filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)}

    # return max(dict_, key=lambda k: dict_[k])
    return dict_


def find_farthest_orbit2(list_of_orbits: list) -> list:
    ellipse_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits))
    square = list(map(lambda orbit: round(pi * orbit[0] / 2 * orbit[1] / 2, 2), ellipse_orbits))
    orbits_data = list(zip(ellipse_orbits, square))

    return max(orbits_data, key=lambda x: x[1])


num = int(input("Введите количество планет:"))
orbits = [(random.randint(1, 10), random.randint(1, 10)) for i in range(num)]
print(orbits)

print(*find_farthest_orbit2(orbits))


# dict_p = find_farthest_orbit(orbits)
# print(max(dict_p), dict_p[max(dict_p)])


def find_farthest_orbit3(lst):
    return max(list(map(lambda item: (item, round(pi * item[0] / 2 * item[1] / 2, 2)),
                        list(filter(lambda item: item[0] != item[1], lst)))), key=lambda x: x[1])


print(find_farthest_orbit3(orbits))

print(max(map(lambda item: (item, item[0] * item[1]), filter(lambda item: item[0] != item[1],
                                                             orbits1 := [(random.randint(1, 10), random.randint(1, 10))
                                                                         for _ in
                                                                         range(int(input("Введите колво планет: ")))])),
          key=lambda item: item[1]), orbits1)
