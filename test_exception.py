# -*- coding:utf-8 -*-
import traceback
import logging


# base of exception class is BaseException

class MyError(ValueError):
    def __str__(self):
        return "My Custom Error"


def ex():
    raise MyError()


def func1():
    ex()


def func2():
    func1()


if __name__ == '__main__':
    try:
        print('hello')
        r = int('a')
        r = 10 / 0
        print('world')
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('No exception')
    finally:
        print('finally')
    print('END')

    try:
        func2()
    except Exception as e:
        print('print ', '*' * 40)
        print(traceback.format_exc())
        # print('exception ', '*' * 40)
        # logging.exception(e)

    # can be cose by -O
    n = 0
    assert n != 0, "n is zero"
