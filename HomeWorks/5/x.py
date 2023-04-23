# *****Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

# Input -> 435467
# Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь

# Задача со звёздочкой...


def get_class_name(class_count: int, number_class: list) -> str:
    name_class_num = {2: "тысяч", 3: "миллион", 4: "миллиард", 5: "триллион", 6: "квадриллион", 7: "квинтиллион",
                      8: "секстиллион"}

    class_name = name_class_num[class_count]

    class_length = len(number_class)

    if class_count == 2:
        if number_class[-1] == 1 and (class_length == 1 or number_class[-2] != 1):
            class_name += "а"
        elif number_class[-1] in [2, 3, 4] and (class_length == 1 or number_class[-2] != 1):
            class_name += "и"
    elif class_count > 2:
        if number_class[-1] in [2, 3, 4] and (class_length == 1 or number_class[-2] != 1):
            class_name += "а"
        elif number_class[-1] == 1 and (class_length == 1 or number_class[-2] != 1):
            pass
        else:
            class_name += "ов"

    return class_name


def convert_number_in_words(num: int) -> str:
    units = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
             9: "девять", 11: "одна", 12: "две"}

    dozens = {1: "десять", 2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят", 6: "шестьдесят", 7: "семьдесят",
              8: "восемьдесят", 9: "девяносто"}

    hundreds = {1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот", 6: "шестьсот",
                7: "семьсот", 8: "восемьсот", 9: "девятьсот"}

    first_dozen = {11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
                  16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}

    if num == 0:
        return units[num]

    num_words = ""
    num_list = list(map(int, str(num)))
    length = len(num_list)

    # обход классов числа
    for class_count in range(1, length // 3 + (1 if length % 3 else 0) + 1):
        pos2 = length - 3 * (class_count - 1)
        pos1 = pos2 - 3
        num_class = num_list[pos1 if pos1 > 0 else 0: pos2]
        class_length = len(num_class)
        num_words_class = ""

        # обход цифр в классе
        for i in range(class_length):
            if i == 0 and num_class[-1] != 0:
                if class_length == 1 or num_class[-2] != 1:
                    num_words_class = units.get(num_class[-1] + (
                        10 if class_count == 2 and 2 >= num_class[-1] >= 1 and (
                                class_length == 1 or num_class[-2] != 1) else 0)) + (
                                          " " if num_words_class else "") + num_words_class
            elif i == 1 and num_class[-2] != 0:
                if num_class[-2] == 1 and num_class[-1] > 0:
                    num_words_class = first_dozen.get(num_class[-2] * 10 + num_class[-1]) + (
                        " " if num_words_class else "") + num_words_class
                else:
                    num_words_class = dozens.get(num_class[-2]) + (" " if num_words_class else "") + num_words_class
            elif i == 2 and num_class[-3] != 0:
                num_words_class = hundreds.get(num_class[-3]) + (" " if num_words_class else "") + num_words_class
            # else:
            #     pass

        if num_words_class:
            num_words = num_words_class + (
                " " + get_class_name(class_count, num_class) + " " if class_count > 1 else "") + num_words

    return num_words


while True:
    number = input("Введите число: ")

    if not number:
        print("БЛАГОДАРЮ ЗА ВНИМАНИЕ !!!")
        break

    if int(number) < 1_000_000_000_000_000_000_000_000:
        print(convert_number_in_words(int(number)))
