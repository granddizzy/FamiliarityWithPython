# Задача №25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# input_str = input("Введите строку: ")
input_str = "aaabcaadcdd"

list1, dict1 = [], {}

for symbol in input_str:
    # if symbol in dict1:
    #     list1.append(symbol + "_" + str(dict1[symbol]))
    # else:
    #     list1.append(symbol)

    list1.append(symbol + "_" + str(dict1[symbol])) if symbol in dict1 else list1.append(symbol)
    dict1[symbol] = dict1.get(symbol, 0) + 1

print(" ".join(list1))
