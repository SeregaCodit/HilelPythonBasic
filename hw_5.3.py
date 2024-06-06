"""
Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

Декілька правил:

ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
підсумкова довжина hashtag має бути не більше 140 символів.
кожне слово починається з великої літери.
якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
"""

import string

excepted_symbols = string.punctuation
user_input = input("write any string: ").strip()

for i in excepted_symbols:
    user_input = user_input.replace(i, "")

splited_user_input = user_input.split()
hashtag = "#" + "".join([i.title() for i in splited_user_input])
hashtag = hashtag[:140]
print(hashtag)
