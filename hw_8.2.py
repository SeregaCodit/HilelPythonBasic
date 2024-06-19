"""
Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.

Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.

Функція приймає на вхід рядок, та повертає булеве значення True або False
"""

from string import ascii_letters
from string import digits


def is_palindrome(text):
    normalized_text = "".join([i for i in text if i in ascii_letters + digits]).lower()
    return normalized_text == normalized_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
