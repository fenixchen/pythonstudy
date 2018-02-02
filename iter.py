# -*- coding:utf-8 -*-

from collections import Iterable

if __name__ == '__main__':
    print(isinstance((x for x in range(10)), Iterable))
    print(isinstance([1,2,3], Iterable))
