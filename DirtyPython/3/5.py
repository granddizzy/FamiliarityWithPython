# 5. Вводим сегодняшнюю дату и сегодняшний день недели, затем вводим новую дату и программа должна выдать нам какой день недели будет в эту дату

# григорианский календарь предусматривает, что год, который делится без остатка на 100 (например, 1900)
# является високосным годом только в том случае, если он также без остатка делится на 400.
# not year % 4 or (not year % 100 and not year % 400):
# 365 ... 366

def is_leap_year(year):
    return not year % 4 or (not year % 100 and not year % 400)


week_days = {1: "Понедельник", 2: "Вторник", 3 : "Среда", 4 : "Четверг", 5: "Пятница", 6: "Суббота", 0: "Воскресенье"}
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

day_of_the_week = 4  # четверг
start_date_list = list(map(int, "01.07.1970".split(".")))

# input_date = list(map(int, input("Введите дату DD.MM.YYYY: ").split(".")))
input_date = "16.04.2023"
input_date_list = list(map(int, input_date.split(".")))

diff_days = 0

# подведем к началу следующего года (если стартовая дата не с начала года)
if start_date_list[0] != 1 or start_date_list[1] != 1:
    leapyear_repair = 1 if is_leap_year(start_date_list[2]) else 0

    # добавляем дни месяца
    diff_days += month_days[start_date_list[1]] + leapyear_repair if start_date_list[1] == 2 else 0

    # добавляем оставшиеся месяцы
    for month in range(start_date_list[1]+1, 13):
        diff_days += month_days[month] + leapyear_repair if month == 2 else 0

# количество полных лет
diff_days = sum([366 if is_leap_year(year) else 365 for year in range(start_date_list[2], input_date_list[2])])

leapyear_repair = 1 if is_leap_year(input_date_list[2]) else 0

# количество полных месяцев в неполном году
for month in range(1, input_date_list[1]):
    diff_days += month_days[month] + (leapyear_repair if month == 2 else 0)

# количество дней в неполном месяце
diff_days += input_date_list[0] - 1

week_day = (diff_days + day_of_the_week) % 7 if diff_days + day_of_the_week > 6 else diff_days + day_of_the_week

print(f"День недели {input_date} - {week_days[week_day]}")
