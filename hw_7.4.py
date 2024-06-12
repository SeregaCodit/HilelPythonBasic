"""
Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за
 наступними правилом:

Один список з числами кратними 3, інший з кратними числами 5.

За допомогою множин створіть набір з числами, які є в обох множинах (перетин).

Функція повинна повернути цю множину як результат своєї роботи.
"""


def create_set(multiplicity: int, length: int = 100) -> set:
    result = [i for i in range(0, length, multiplicity)]
    return set(result)


def common_elements() -> set:
    set1 = create_set(multiplicity=3)
    set2 = create_set(multiplicity=5)
    return set1.intersection(set2)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print("OK")
