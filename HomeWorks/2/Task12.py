# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
import random

x1 = int(random.randint(1, 1000))
y1 = int(random.randint(1, 1000))

s = int(x1 + y1)
p = int(x1 * y1)

# s = x + y
# p = x * y
for x in range(1, 1001):
    y = s - x

    if x * y == p:
        print(f"Отгаданные числа {x} и {y}")
        break
else:
    print("Чисел удовлетворяющих условию не существует!!!")

print("Загаданные числа", x1, "и", y1)

# математическое решение
# s = x + y
# p = x * y
# p = y(s-y) = ys - y**2
# p = x * (s-x) = xs - x**2
# x**2 - sx + p = 0

# Квадратное уравнение — это уравнение вида ax2 + bx + c = 0, где a — первый или старший коэффициент, не равный нулю, b — второй коэффициент, c — свободный член.
# Дискриминант квадратного уравнения — это выражение, D = b**2 − 4ac
# D<0 корней нет
# D=0 один корень x=−b/2a.
# D>0 два корня x=-b+D**0.5/2a x=-b-D**0.5/2a

# a = 1
# b = -s
# c = p

d = -s**2 - 4 * p

if d >= 0:
     y = (s + d**0.5) / 2
     x = s - y
     print(f"Отгаданные числа {int(x)} и {int(y)}")
else:
    print("Чисел удовлетворяющих условию не существует!!!")

