# -*- coding:utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('>>before %s' % func.__name__)
        ret = func(*args, **kw)
        print('<<after %s' % func.__name__)
        return ret

    return wrapper


def log2(prompt):
    def decorator(func):
        @functools.wraps(func) #keep name same
        def wrapper(*args, **kw):
            print('>>before %s %s' % (prompt, func.__name__))
            ret = func(*args, **kw)
            print('>>after %s %s' % (prompt, func.__name__))
            return ret

        return wrapper

    return decorator


@log
@log2('CALL')
def hello():
    print("Hello")


'''
same as now = log(now)
now()
'''

if __name__ == '__main__':
    hello()
    print(hello)
    print(hello.__name__)
