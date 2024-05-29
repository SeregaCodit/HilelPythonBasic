"""
На запит від програми, користувач вводить 5-ти значне ціле, позитивне число. Вам необхідно "перевернути" цє число задом
 наперед, тобто щоб у результаті вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.

Вам не потрібно перевіряти, що користувач ввів правильне число - зробіть вигляд, що користувач завжди вводить 5 значне
число. Тобто введене користувачем число завжди складатиметься з 5 цифр.

Якщо користувач ввів інше число, це проблема користувача, а не вашої програми.

Використовуються лише цілі числа.

Для розв'язання задачі потрібно використовувати лише той зріз даних, який було пройдено. Тобто використовувати строки не
можна.

Приклади:

Користувач ввів: 12345 - на екрані відображається: 54321

Користувач ввів: 37568 - на екран відображається: 86573
"""

delimiter = 10
exp = 4
user_input = int(input("введіть п'ятизначне число: "))

digit1 = user_input % delimiter
digit1 *= delimiter ** exp
# digit1 = digit1 * 10000
exp -= 1
user_input //= delimiter

digit2 = user_input % delimiter
digit2 *= delimiter ** exp
# digit2 = digit2 * 1000
exp -= 1
user_input //= delimiter

digit3 = user_input % delimiter
digit3 *= delimiter ** exp
exp -= 1
user_input //= delimiter

digit4 = user_input % delimiter
digit4 *= delimiter ** exp
exp -= 1
user_input //= delimiter

digit5 = user_input % delimiter

result = digit1 + digit2 + digit3 + digit4 + digit5

print(result)



