"""
Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом. До нього необхідно додати 1.

Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму, знову розбити на список із цифр.

В результаті функція повертає список із цифр, що становлять значення суми.

Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235. Після цього потрібно розбити отримане число на складові цифри. У результаті має бути список [1, 2, 3, 5], який повертає функція.

* модифікувати похідний список, а не створювати новий
"""


def add_one(some_list):
    some_list[-1] += 1
    for i in range(len(some_list) - 1, -1, -1):
        if some_list[i] > 9:
            some_list[i] = 0
            if i > 0:
                some_list[i - 1] += 1
            else:
                some_list.insert(0, 1)
    return some_list


# def add_one(some_list, index=-1) -> list:
#     # God bless recursion
#     if index < -len(some_list):
#         some_list.insert(0, 1)
#         some_list[index + 1] = 0
#         return some_list
#
#     some_list[index] += 1
#     if some_list[index] < 10:
#         return some_list
#
#     some_list[index] = 0
#     index -= 1
#     add_one(some_list, index)
#     return some_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9,  9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
