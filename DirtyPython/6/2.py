# выдать топ 5 самых встречаемы слов в Алисе длинна которых не меньше 5 букв
import string

with open("Alice in Wonderland.txt", "r", encoding="UTF-8") as file:
    text_ = file.read().lower()

for sym in string.punctuation + "\n\xa0" + "1234567890«»-–":
    text_ = text_.replace(sym, "")

words = text_.split()
dict_words = {word: words.count(word) for word in set(words)}

# print(max(dict_words, key=lambda k: dict_words[k]))

sorted_tuples = sorted(dict_words.items(), key=lambda el: el[1])

for item in sorted_tuples:
    print(*item, sep=" - ")
