"""
Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження шуканого рядка у рядку
для пошуку.

Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims". Якби нам треба було знайти її перше
 входження, то тут все просто: за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у
 слові "sims", а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s", а вона четверта за
 рахунком. Значить індекс другого входження (і у відповідь питання) дорівнює 3.

Рядок, який потрібно знайти, може складатися з кількох символів.

Input: Два рядки (String).

Output: Int or None
"""


def get_error_message(condition_dict) -> str:
    #повторення словників та рядків
    message = ""
    for key in condition_dict:
        val, val_type = condition_dict[key]
        if not isinstance(val, val_type):
            message += f"{key} must be {val_type}, got {type(val)}\n"
    return message


def second_index(text: str, some_str: str, occurrence: int = 2) -> str | int | None:  #трошки ускладнив: шукає будь яке входження
    condition_dict = {"text": (text, str), "some_str": (some_str, str), "target_index": (occurrence, int)}
    error_message = get_error_message(condition_dict)
    if error_message:
        return error_message

    index = -1
    for i in range(occurrence):
        index = text.find(some_str, index + 1)

    return index if index != -1 else None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
assert second_index("Hello, hello", "l", 4) == 10, 'Test5'
print('ОК')
