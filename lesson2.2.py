"""
Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик
цифр, з якого це число складається. Наприклад, користувач вводить 1234, а програма виводить:

1

2

3

4

Завдання необхідно вирішити, використовуючи методи поділу (підказка // і % або divmod). Виведення в стовпчик можна
зробити за допомогою 4-х функцій print.

Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число, яке складається з 4-х цифр,
де кожна цифра може бути від 0 до 9 включно.

Ваше рішення має це враховувати! Якщо користувач ввів не ціле число, це проблема користувача, а не вашої програми.

Створюйте рішення, виходячи з того, що число ЗАВЖДИ 4-х значне.
"""

delimiter = 1000
user_input = input("введіть чотирьохзначне число: ")
value = int(user_input)


quotient, remainder = divmod(value, delimiter)
print(quotient)
delimiter /= 10

quotient, remainder = divmod(remainder, delimiter)
print(int(quotient))
delimiter /= 10

quotient, remainder = divmod(remainder, delimiter)
print(int(quotient))
delimiter /= 10

quotient, remainder = divmod(remainder, delimiter)
print(int(quotient))


