import codecs
from functools import wraps
import inspect


def get_named_arguments(func):
    signature = inspect.signature(func)
    return {param.name: param.default for param in signature.parameters.values() if param.default != param.empty}


def write_to_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_file = kwargs.get('result_file')
        if result_file is None:
            default_arguments = get_named_arguments(func)
            result_file = default_arguments["result_file"]
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(result)
        return result
    return wrapper


@write_to_file
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleared = []
    splitted_html = [i for i in html.split("<")]
    for i in splitted_html:
        index = i.find(">")
        if index != -1:
            i = i[index + 1:]
            if not i.startswith("\n") and i:
                cleared.append(i)

    return "\n".join(cleared)


delete_html_tags(html_file="draft.html")
