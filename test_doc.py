# -*- coding:utf-8 -*-



class Adder(object):
    '''
    simpel adder
    >>> adder = Adder()
    >>> adder.add(1)
    >>> adder.add(2)
    >>> adder.get_value()
    3
    >>> adder.add(3)
    >>> adder.get_value()
    10
    '''
    def __init__(self):
        self.value = 0

    def add(self, value):
        self.value = self.value + value

    def get_value(self):
        return self.value

if __name__ == '__main__':
    import doctest
    doctest.testmod()