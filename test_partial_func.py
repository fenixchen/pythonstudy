# -*- coding:utf-8 -*-


import functools


def add(x, y):
    return x + y


if __name__ == '__main__':
    x = 2
    y = 3
    add2 = functools.partial(add, y=10)
    print(add(x, y))
    print(add2(x))
