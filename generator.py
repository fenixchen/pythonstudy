# -*- coding:utf-8 -*-


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # return here, and next call continue
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    L = [x * x for x in range(10)]
    print(L)

    g = (x * x for x in range(10))
    print(type(g))
    for i in range(10):
        print(next(g))

    g = (x * x for x in range(10))
    for i in g:
        print(i)

    print('*' * 20)
    fib(10)

    print('*' * 20)
    for i in fib_generator(10):
        print(i)

    g = fib_generator(6)
    while True:
        try:
            x = next(g)
            print('g', x)
        except StopIteration as e:
            print('return', e.value)
            break
