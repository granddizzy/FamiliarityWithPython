# В 4-значном числе поменять местами первую и последнюю цифру
# Попробовать решить максимальным количеством разных способов

number = input("Введите число: ")

print(number)

if len(number) > 1:
    number = number[len(number)-1] + number[1: len(number)-1] + number[0]

print(number)

list_number = list(number)

if len(number) > 1:
    temp = list_number[0]
    list_number[0] = list_number[len(list_number)-1]
    list_number[len(list_number)-1] = temp

print(number)

if len(number) > 1:
    new_str = number[len(number)-1]
    for i in range(1, len(number)):
        new_str += number[i]

    new_str += number[0]

print(number)