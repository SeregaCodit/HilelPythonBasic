from typing import Iterable, Dict


def popular_words(text: str, words: Iterable) -> Dict[str, int]:
    splitted_text = text.lower().split()
    target_words = {key: 0 for key in words}

    for i in splitted_text:
        if i in target_words:
            target_words[i] += 1
    return target_words


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
