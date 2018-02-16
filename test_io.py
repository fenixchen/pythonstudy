# -*- coding:utf-8 -*-

from io import StringIO, BytesIO
import os

FILE = r'e:\hello.txt'
if __name__ == '__main__':
    with open(FILE, 'w') as f:
        f.write('hello \n\nworld')

    with open(FILE, 'r') as f:
        ret = f.read()
        print(ret)

    with open(FILE, 'r') as f:
        print(f.readlines())

    with open(FILE, 'rb') as f:
        b = f.read()
        print(type(b))
        print(b)

    print('StringIO', '*' * 40)
    f = StringIO()
    f.write('hello ')
    f.write('world')
    print(f.getvalue())

    f = StringIO('How\nAre\nYou')
    print(f.readlines())

    print('BytesIO', '*' * 40)
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())

    print('OS', '*' * 40)
    print(os.name)
    print(os.environ)
    print(os.environ['PATH'])
    print(os.path.abspath('.'))
    p = os.path.join('world', 'hello.txt')
    print(p)
    print(os.path.split(p))
    print(os.path.splitext(p))
    d = [x for x in os.listdir('e:\\') if os.path.isdir('e:\\' + x)]
    print(d)