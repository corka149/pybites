from functools import wraps


def int_args(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            if arg < 0:
                raise ValueError
        return func(*args, **kwargs)
    return new_func
