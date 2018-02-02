# -*- coding:utf-8 -*-


if __name__ == '__main__':
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)
    print(classmates[-1])
    print(len(classmates))
    classmates.pop(-1)
    print(classmates)

    # slice
    a = [1,2,3,4,5]
    print(a[0:3])
    print(a[-3:-1])

    b = list(range(100))
    print(b)
    print(b[-10:])

    str = "abcdefgh"
    print(str[3:6])