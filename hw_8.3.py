"""
Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та
 повертати його. Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде
  кілька унікальних чисел, перевіряти не потрібно.
"""
from collections import Counter


def fill(data: list) -> dict:
    result_dict = {}
    for i in data:
        result_dict[i] += 1 if i in result_dict else 1
    return result_dict


def find_unique_value(some_list):
    count_dict = fill(some_list)
    for i in count_dict:
        if count_dict[i] == 1:
            return i


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
