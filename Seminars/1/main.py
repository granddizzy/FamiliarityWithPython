#За день машина проезжает n километров.
#Сколько дней нужно, чтобы проехать маршрут длиной m километров?
#При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# m = input("km in day:")
# n = input("km:")
#
# a = int(n) / int(m)
#
# print ("Need {} days".format(a))

# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# import math
#
# a = 33
# b = 23
# c = 35
#
# count = math.ceil(float(a) / 2) + math.ceil(float(b) / 2) + math.ceil(float(c) / 2)
#
# print ("Min count of parts {}".format(count))

# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# i = 3
# j = 4
#
# if i == j:
#     print ("unknoun");
# else:
#     print(j+i-1);


#Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
#Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
#год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

year = int(input("Input year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print ("yes")
else:
    print("no")