"""
На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так, щоб вони завжди
починалися з великої літери та закінчувалися крапкою.

Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не потрібно, це
 буде помилкою

Вхідні аргументи: string.

Вихідні аргументи: string.
"""


def convert_to_capitalize(text: str) -> str:
    sentences_list = text.split(". ")
    sentences_list = [i.capitalize() for i in sentences_list]
    return ". ".join(sentences_list)


def add_last_symbol(text: str, symbol: str = ".") -> str:
    if text.endswith(symbol):
        return text
    return f"{text}{symbol}"


def correct_sentence(text: str) -> str:
    if not isinstance(text, str):
        return f"text must be a string, got {type(text)}"

    if not text:
        return text

    text = convert_to_capitalize(text)
    text = add_last_symbol(text)
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
