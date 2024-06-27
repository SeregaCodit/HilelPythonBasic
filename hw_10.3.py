from functools import wraps


def is_binary_even(func):
    #попрактикуватись із декораторами
    @wraps(func)
    def wrapper(digit) -> bool:
        last_bit = digit & 1
        return not last_bit
    return wrapper


@is_binary_even
def is_even(digit):
    """ Перевірка чи є парним число """
    return digit


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
