"""
Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та
 повертати його. Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде
  кілька унікальних чисел, перевіряти не потрібно.
"""
from collections import Counter


def find_unique_value(some_list):
    counted_items = Counter(some_list)
    for key, val in counted_items.items():
        if key == 1:
            return val


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
