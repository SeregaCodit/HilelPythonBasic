"""
Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.

Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
"""
import random


random_list = [random.randint(0,9) for i in range(random.randint(3, 10))]
print(len(random_list))
print(random_list, end=" == ")

second_from_the_end = len(random_list) - 2
target_index_list = [0, 2, second_from_the_end]
result_list = [random_list[i] for i in target_index_list]
print(result_list)
