# 2. Мы уже делали переводчик числа из десятичной в двоичную в двоичную,
# самое время сделать для восьмиричной и шестнадцатиричной.
# а лучше сделать универсальный (двоичная, восьмиричная, шеснадцатиричная) и подумать как интереснее оформить "меню" выбора в какую систему переводим:)

def convert(basis, number):
    number_in_basis = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while number > 0:
        n = number % basis
        number_in_basis = (str(n) if n < 10 else alphabet[n - 10]) + number_in_basis
        number //= basis

    return number_in_basis


number = int(input("Введите число : "))
basis = int(input("Введите основание системы исчисления в которую хотите перевести (BIN - 2, OCT - 8, HEX - 16): "))

print(f"Число в системе с основанием {basis}: {convert(basis, number)}")
