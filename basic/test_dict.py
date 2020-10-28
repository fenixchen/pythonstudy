# -*- coding:utf-8 -*-

from collections import Iterable

if __name__ == '__main__':
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])
    if 'Bob' in d:
        print(d['Bob'])
    print(d.get('Hello'))
    d.pop('Bob')
    print(d)
    # only string, int can be key

    set = set([1, 2, 3])
    print(set)
    set.add(1)
    print(set)
    set.remove(2)
    print(set)

    # set.add([1,2]) #unhashable type

    # str is invariant
    a = 'abc'
    b = a.replace('a', 'A')
    print(a)
    print(b)

    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for i in a:
        print(i, "=>", a[i])

    for i in a.values():
        print(i)

    print(isinstance(a, Iterable))
    print(isinstance('abc', Iterable))
    print(isinstance(123, Iterable))

    for key, value in enumerate(a):
        print(key, "=>", value)

    b = [1, 2, 4, 8]
    for i, n in enumerate(b):
        print(i, n)

    c = [(1, 2), (3, 4), (5, 6)]
    for j, k in c:
        print(j, k)

    for i in [x * x for x in range(1, 11)]:
        print(i)

    for i in [x * x for x in range(1, 11) if x % 2 == 0]:
        print(i)

    for x in [m * n for m in range(1, 10) for n in range(1, 10)]:
        print(x)

    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for k, v in a.items():
        print(k, "=>", v)

    for l in [k + '->' + str(v) for k, v in a.items()]:
        print(l)

    a = ['Hello', 'worlD']
    b = [ x.lower() for x in a]
    print(b)

    a = ['Hello', 'worlD', 123, True]
    c = [x.lower() for x in a if isinstance(x, str)]
    print(c)