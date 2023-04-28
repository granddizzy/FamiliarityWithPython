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

from math import pi


def find_farthest_orbit(list_of_orbits: list) -> tuple:
    max_orbit = tuple()
    max_square = 0
    for orbit in list_of_orbits:
        if orbit[0] == orbit[1]:
            continue

        square = round(pi * orbit[0] / 2 * orbit[1] / 2, 2)
        if square > max_square:
            max_square = square
            max_orbit = orbit

    return max_orbit


def find_farthest_orbit2(list_of_orbits: list) -> tuple:
    dict_ = {orbit: round(pi * orbit[0] / 2 * orbit[1] / 2, 2) for orbit in
             filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)}

    return max(dict_, key=lambda k: dict_[k])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
print(*find_farthest_orbit2(orbits))
