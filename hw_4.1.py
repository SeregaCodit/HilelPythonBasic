"""
Написати програму, яка переміщає всі нулі у кінець списку.

Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.

Порядок ненульових чисел має зберегтися!
"""
import random

list_length = 10
last_index_in_list = list_length - 1

# створюємо не пустий список
lst = [random.randint(0, i) for i in range(random.randint(1, list_length))]

# забезпечуємо, що у списку будуть нулі
if 0 not in lst:
    iterations = random.randint(1, int(list_length / random.randint(1, last_index_in_list)))
    for i in range(iterations):
        index = random.randint(0, last_index_in_list)
        if lst[index]:
            lst[index] = 0

print("original list", lst, sep=": ", end=" => ")

count_of_zeros = lst.count(0)
lst = [i for i in lst if i]
lst += [0] * count_of_zeros

print("result list", lst, sep=": ")
