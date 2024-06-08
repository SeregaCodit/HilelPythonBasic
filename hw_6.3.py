"""
Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа, поки воно не стане
 менше або дорівнювати 9.

Користувач вводить число з клавіатури.

Приклади:

Copy code
999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126,
 потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
1000 -> 0
423 -> 8
33 -> 9
25 -> 0
1 -> 1
"""
import random

random_method = False
accessible_inputs = ["1", "2"]

user_input = input("type a number: ")
result = f"{user_input} -> "
method = input("[choose calculation method]: 1 for evaluate, 2 for 'no pain - no gain' method: ")

while method not in accessible_inputs:
    if random_method:
        method = random.choice(accessible_inputs)

    if method == "1":
        while int(user_input) > 9:
            operation = "*".join(list(str(user_input)))
            user_input = eval(operation)
        result += str(user_input)
    elif method == "2":
        value = 1
        while len(user_input) != 1:
            for i in list(user_input):
                value *= int(i)
            user_input = str(value)
            value = 1
        result += str(user_input)
    else:
        result = "\nif you don't care about letters, then I don't care about letters either\n" + result
        random_method = True


print(result)
