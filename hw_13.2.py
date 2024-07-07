from functools import wraps


class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    @staticmethod
    def check_value(func):
        @wraps(func)
        def wrapper(_, value, **kwargs):
            if isinstance(value, int):
                kwargs["is_int"] = True
            else:
                kwargs["is_int"] = False
            return func(_, value, **kwargs)

        return wrapper

    @staticmethod
    def value_to_int(func):
        @wraps(func)
        def wrapper(_, value, **kwargs):
            if kwargs["is_int"]:
                return func(_, value, **kwargs)
            try:
                value = int(value)
            except (ValueError, TypeError):
                print(f"Function {func.__name__}() accepts only numbers, not a {type(value)}!")
                return None

            return func(_, value, **kwargs)

        return wrapper

    @staticmethod
    def validate_value(func):
        @wraps(func)
        def wrapper(instance, value, **kwargs):
            if func.__name__ == "set_current":
                if instance.min_value <= value <= instance.max_value:
                    return func(instance, value, **kwargs)
                else:
                    raise ValueError(f"current value must be >= {instance.min_value} and"
                                     f" <= {instance.max_value}")
            elif func.__name__ == "set_min":
                if value <= instance.current and value <= instance.max_value:
                    return func(instance, value, **kwargs)
                else:
                    raise ValueError(f"min value must be <= {instance.current}")

            elif func.__name__ == "set_max":
                if value >= instance.current and instance.max_value:
                    return func(instance, value, **kwargs)
                else:
                    raise ValueError(f"max value must be >= {instance.current}")
            else:
                raise NameError(f"Дідько! Я хз що робити з функцією {func.__name__}! Шукай того хто це писав!")

        return wrapper

    @staticmethod
    def check_limits(func):
        @wraps(func)
        def wrapper(instance):
            if instance.min_value < instance.current < instance.max_value:
                return func(instance)
            elif instance.min_value != instance.current and func.__name__ == "step_down":
                return func(instance)
            elif instance.max_value != instance.current and func.__name__ == "step_up":
                return func(instance)
            else:
                limit = "minimum" if func.__name__ == "step_down" else "maximum"
            raise ValueError(f"counter {limit} is reached!")

        return wrapper

    @check_value
    @value_to_int
    @validate_value
    def set_current(self, start, **kwargs):
        self.current = start

    @check_value
    @value_to_int
    @validate_value
    def set_max(self, max_max, **kwargs):
        self.max_value = max_max

    @check_value
    @value_to_int
    @validate_value
    def set_min(self, min_min, **kwargs):
        self.min_value = min_min

    @check_limits
    def step_up(self):
        self.current += 1

    @check_limits
    def step_down(self):
        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
