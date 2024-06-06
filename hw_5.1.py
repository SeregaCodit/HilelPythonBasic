"""
Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.

Змінна не може:

починатися з цифри
містити великі літери,
пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
бути жодним із зареєстрованих слів.
При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".

Список зареєстрованих слів можна взяти із keyword.kwlist.

У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
"""
import keyword
import string

variable_name_is_reserved = False
excepted_symbol_is_in_variable_name = False
start_with_digit = False
excepted_words = keyword.kwlist
excepted_symbols = " " + string.punctuation.replace("_", "")
digits = "1234567890"
variable_name = input("enter a variable name: ")

for i in excepted_words:
    if i == variable_name:
        variable_name_is_reserved = True
        break

for i in excepted_symbols:
    if i in variable_name:
        excepted_symbol_is_in_variable_name = True
        break

for i in digits:
    if variable_name.startswith(i):
        start_with_digit = True
        break

conditions = [variable_name, not excepted_symbol_is_in_variable_name, variable_name == variable_name.lower(),
              not start_with_digit, not (variable_name.count("_") == len(variable_name) and len(variable_name) > 1),
              not  variable_name_is_reserved]
result = all(conditions)



print(result)
