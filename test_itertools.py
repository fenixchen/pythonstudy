# -*- coding:utf-8 -*-

import itertools

if __name__ == '__main__':
    nat = itertools.count(1)
    print(type(nat), '\t', nat)
    for n in range(10):
        print(next(nat))

    cs = itertools.cycle('ABCDEF')
    for n in range(10):
        print(next(cs))

    ns = itertools.repeat('B', 10)
    for n in ns:
        print(n)

    nat = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, nat)
    print(list(ns))

    for c in itertools.chain('ABC', 'XYZ'):
        print(c)

    for key, group in itertools.groupby('AAABBBCCAAA'):
        print(key, list(group))

    for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
        print(key, list(group))