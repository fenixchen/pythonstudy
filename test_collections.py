# -*- coding:utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict


if __name__ == '__main__':
    print('<<namedtuple>>', '*' * 40)
    Point = namedtuple('Point', ['x', 'y'])
    print(type(Point))
    print(Point)
    print(Point.__dict__)
    p = Point(10, 20)
    print(p, p.x, p.y)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))

    print('<<deque>>', '*' * 40)
    q = deque([1,2,3])
    q.append(4)
    q.appendleft(5)
    print(q)

    print('<<defaultdict>>', '*' * 40)
    d = defaultdict(int)
    d['A'] = 10
    d['B'] = 20
    print(d['A'])
    d['C'] += 100
    print(d['C'])

    print('<<OrderedDict>>', '*' * 40)
    d = dict(a=1, b=2, d=4, c=3)
    print(d)
    od = OrderedDict()
    od['A'] = 1
    od['C'] = 10
    od['D'] = 100
    od['E'] = 1000
    print(od)

