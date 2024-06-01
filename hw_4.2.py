"""
Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд], потім перемножити цю суму на останній елемент вхідного масиву.

Не забудьте, що перший елемент масиву має індекс 0.

Для порожнього масиву результат завжди 0.
"""
import random

while True:
    user_input = input("enter the list length to process, or press enter for exit: ")

    if user_input == "":
        print("End.")
        break

    # вважаємо, що користувач завжди вводить число
    lst_length = int(user_input)
    lst = [random.randint(-100 , 100) for i in range(random.randint(0, lst_length))]
    print(lst, end=" => ")

    if lst:
        multiplier = lst[-1]
        even_index_list = [i[1] for i in enumerate(lst) if i[0] % 2 == 0]
        result = sum(even_index_list) * multiplier
    else:
        result = 0

    print(result, end="\n" * 2)