# -*- coding:utf-8 -*-

import re

if __name__ == '__main__':
    print('\n<<match>>', '*' * 40)
    ret = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    print(ret)
    ret = re.match(r'^\d{3}\-\d{3,8}$', '010-12346711312')
    print(ret)

    print('\n<<split>>', '*' * 40)
    s = 'a b    c'
    print(s.split(' '))
    print(re.split(r'\s+', s))
    s = 'a b    c,d,e'
    print(re.split(r'[\s,]+', s))

    print('\n<<group>>', '*' * 40)
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print(m)
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.groups())

    print('\n<<greed match>>', '*' * 40)
    print(re.match(r'^(\d+)(0*)$', '102300').groups())
    print(re.match(r'^(\d+?)(0*)$', '102300').groups()) # ? character

    print('\n<<compiling>>', '*' * 40)
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    print(re_telephone.match('010-12345').groups())