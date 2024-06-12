"""
Написати програму, яка переміщає всі нулі у кінець списку.

Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.

Порядок ненульових чисел має зберегтися!
"""
import random
list_length = 10
# створюємо список
lst = [random.randint(0, i) for i in range(random.randint(1, list_length))]

# забезпечуємо, що у списку прнайнє один елемент дорівнює нулю
if 0 not in lst:
    iterations = random.randint(1, int(list_length / random.randint(1, list_length - 1)))
    for i in range(iterations):
        index = random.randint(0, list_length - 1)
        if lst[index]:
            lst[index] = 0

print(f"original list", lst, sep=": ", end=" => ")

for i in lst:
    if i == 0:
        tmp = lst.pop(lst.index(i))
        lst.append(tmp)

print("result list", lst, sep=": ")