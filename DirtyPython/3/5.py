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
begin_day, begin_month, begin_year = list(map(int, "01.07.1970".split(".")))

input_date = input("Введите дату DD.MM.YYYY: ")
end_day, end_month, end_year = list(map(int, input_date.split(".")))

diff_days = 0

# подведем к началу следующего года (если стартовая дата не с начала года)
if begin_day != 1 or begin_month != 1:
    leapyear_repair = 1 if is_leap_year(begin_year) else 0

    # добавляем дни месяца
    diff_days += month_days[begin_month] + leapyear_repair if begin_month == 2 else 0

    # добавляем оставшиеся месяцы
    for month in range(begin_month + 1, 13):
        diff_days += month_days[month] + leapyear_repair if month == 2 else 0

# количество дней полных лет
diff_days = sum([366 if is_leap_year(year) else 365 for year in range(begin_year, end_year)])

leapyear_repair = 1 if is_leap_year(end_year) else 0

# количество дней полных месяцев в неполном году
for month in range(1, end_month):
    diff_days += month_days[month] + (leapyear_repair if month == 2 else 0)

# количество дней в неполном месяце и корректировка на день недели
diff_days += end_day - day_of_the_week

week_day = diff_days % 7 if diff_days > 6 else diff_days

print(f"День недели {input_date} - {week_days[week_day]}")
