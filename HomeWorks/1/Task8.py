# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите количество долек с одной стороны n: "))
m = int(input("Введите количество долек с другой стороны m: "))
k = int(input("Введите количество долек которые хотите отломить k: "))

if k >= n * m:
    print("Ешь сразу всю :)")
elif k % m == 0 or k % n == 0:
    print("Все получится!!!")
else:
    print("За один раз отломать столько долек не выйдет :(")