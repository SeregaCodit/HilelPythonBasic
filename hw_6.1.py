"""
Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.

Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.

Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
"""

from string import ascii_letters


user_input = input("type an interval: ").replace(" ", "").strip()

start, end = user_input.split("-")
start_index, end_index = ascii_letters.index(start), ascii_letters.index(end) + 1
result = ascii_letters[start_index: end_index]

print(result)
