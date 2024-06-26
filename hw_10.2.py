from string import punctuation


def proceed(data: str, triggers: str) -> str:
    if data[0].isalpha():
        for i in set(data):
            if i in triggers:
                data = data.split(i)[0]
        return data


def first_word(text) -> str | None:
    triggers = punctuation.replace("'", "")
    text = text.strip().split()
    for i in text:
        word = proceed(i, triggers)
        if word:
            return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
