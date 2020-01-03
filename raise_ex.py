import random

n = random.randint(4, 6)


def foo(nnn):
    if nnn == 6:
        raise ValueError('ошибочка нашлась 6 ')
    else:
        return nnn ** 2


try:
    res_foo = foo(n)
    print(res_foo)
except ValueError as a:
    print(a)
