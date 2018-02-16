# -*- coding:utf-8 -*-

from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


def f(x):
    return x * x


def add2(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return ord(s) - ord('0')


def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def create_counter():
    count = 0

    def counter():
        nonlocal count
        count = count + 1
        return count

    return counter


if __name__ == '__main__':
    print(abs(-10))
    print(abs)
    f = abs
    print(f(-10))
    print(add(-1, 3, abs))

    # map
    print('*' * 40)
    l = [x for x in range(10)]
    m = map(f, l)
    print(l)
    print(list(m))
    ls = list(map(str, l))
    print(ls)

    # reduce
    print('*' * 40)
    print(reduce(add2, l))
    print(reduce(add2, ls))

    n = reduce(fn, map(char2num, '12345'))
    print(n)

    m = reduce(lambda x, y: x * 10 + y,
               map(lambda x: ord(x) - ord('0'), '45678'))
    print(m)

    # filter, return Iterator
    print('*' * 40)
    q = list(filter(lambda x: x % 2 == 0, l))
    print(q)

    # primes
    print('*' * 40)
    for n in primes():
        if n < 1000:
            print(n, end=',')
        else:
            break
    print()

    # sort
    print('*' * 40)
    l = [1, -2, 3, -5, 10]
    print(l)
    print(sorted(l))
    print(sorted(l, reverse=True))
    print(sorted(l, key=abs))

    # return function
    print('*' * 40)
    f = lazy_sum(1, 2, 3, 4, 5)
    print(f)
    g = lazy_sum(4, 5, 6, 7, 8)
    print(g)
    print(f())
    print(g())

    counter = create_counter()
    print(counter(), counter(), counter())

    # lambda
    print('*' * 40)
    print(list(map(lambda x: x * x, [y for y in range(10)])))
    f = lambda y: y * 2
    print(f)
    print(f(10))