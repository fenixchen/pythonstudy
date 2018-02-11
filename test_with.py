# -*- coding:utf-8 -*-


from contextlib import contextmanager


class DymmyResource:
    def __init__(self, tag):
        self.tag = tag
        print("New Resource %s" % tag)

    def __enter__(self):
        print("%s Enter" % self.tag)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("%s Exit normally" % self.tag)
        else:
            print("%s Exit exceptionally" % self.tag)


@contextmanager
def MyResourceOpen(tag):
    try:
        print("Enter %s" % tag)
        yield None
    finally:
        print("Exit %s" % tag)


if __name__ == '__main__':
    with DymmyResource('Hello') as hello:
        print("Call hello")
    print('*' * 40)

    try:
        with DymmyResource('world') as world:
            print("Call world 1")
            raise Exception("YYY")
            print("Call world 2")
    except Exception as e:
        print("Exception '%s'" % e)
    print('*' * 40)

    with MyResourceOpen("XXX") as f:
        print("Open")
