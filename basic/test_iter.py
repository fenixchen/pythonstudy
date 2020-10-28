# -*- coding:utf-8 -*-

from collections import Iterable, Iterator

if __name__ == '__main__':
    print(isinstance((x for x in range(10)), Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))

    print(isinstance([1, 2, 3], Iterator))
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))

    print(isinstance(iter([1, 2, 3]), Iterator))
