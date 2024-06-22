def get_min_max(data: set) -> tuple:
    _min, _max = None, None
    if not data:
        return 0, 0
    for i in data:
        if all((_min is None, _max is None)):
            _min = _max = i
        else:
            _min = i if i < _min else _min
            _max = i if i > _max else _max
    return _min, _max


def difference(*args: [int, float]) -> int | float:
    _min, _max = get_min_max({*args})
    return round(_max - _min, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
