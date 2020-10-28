# -*- coding:utf-8 -*-

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


def run(self):
    print('run')


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    h = Hello()
    h.hello()
    print(type(Hello))
    print(type(h))

    # create class
    Dog = type('Dog', (object,), dict(run=run))
    d = Dog()
    d.run()

    L = MyList()
    L.add(1)
    print(L)
