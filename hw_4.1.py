"""
Написати програму, яка переміщає всі нулі у кінець списку.

Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.

Порядок ненульових чисел має зберегтися!
"""
import random

max_list_length = 10

# створюємо не пустий список
lst = [random.randint(0, 10) for i in range(random.randint(1, max_list_length))]
last_index_in_list = len(lst) - 1

# забезпечуємо, що у списку будуть нулі
if 0 not in lst:
    index = random.randint(0, last_index_in_list)
    lst[index] = 0

print("original list", lst, sep=": ", end=" => ")

count_of_zeros = lst.count(0)
lst = [i for i in lst if i]
lst += [0] * count_of_zeros

print("result list", lst, sep=": ")
