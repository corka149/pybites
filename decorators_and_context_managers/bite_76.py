from functools import singledispatch


@singledispatch
def count_down(data_type):
    raise ValueError()


@count_down.register
def _(arg: int):
    while 0 < arg:
        print(arg)
        arg = int(arg / 10)


@count_down.register
def _(arg: str):
    while arg != '':
        print(arg)
        arg = arg[:-1]


@count_down.register
def _(arg: float):
    count_down(str(arg))


@count_down.register
def _(arg: list):
    arg = map(str, arg)
    count_down(''.join(arg))


@count_down.register
def _(arg: tuple):
    arg = map(str, arg)
    count_down(''.join(arg))


@count_down.register
def _(arg: set):
    count_down(sorted(arg))


@count_down.register
def _(arg: dict):
    count_down(list(arg.keys()))


@count_down.register
def _(arg: range):
    count_down(list(arg))
