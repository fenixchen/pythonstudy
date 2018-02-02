# -*- coding:utf-8 -*-


def sub(x, y):
    return x - y


def add_end(L=[]):
    L.append('END')
    return L


def sum(*number):
    print(type(number))
    s = 0
    for n in number:
        s = s + n
    return s


def hello(name, age, **kw):
    print(type(kw))
    print("name:", name, " age:", age, 'other', kw)


def hello2(name, *, city, age):
    print('city:', city)
    print('age:', age)


def hello3(name, *args, **kw):
    print('name:', name)
    for a in args:
        print('a=', a)
    print(kw)


if __name__ == '__main__':
    print(sub(1, 2))
    print(sub(y=1, x=2))

    a = add_end([1, 2, 3])
    print(a)

    # default parameter is variable also
    # should point to invariant
    b = add_end()
    print(b)

    b = add_end()
    print(b)

    # convert to tuple
    print(sum(1, 2, 3))

    print(sum(1, 2, 3, 4))

    numbers = [1, 2, 3]
    # array to variable parameters
    print(sum(*numbers))

    hello('CCH', 12, birthday='1900-1-1')
    # dict to **kw
    info = {'city': 'shanghai',
            'love': 'dog'}
    hello('CL', 29, **info)

    hello2('CCH', city='Hanzhong', age='18')

    arg = (1, 2, 3)
    kw = {'a': 1, 'b': 2}
    hello3('CCH', *arg, **kw)
