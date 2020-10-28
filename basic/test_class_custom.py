# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Student(%s)" % self.__name

    __repr__ = __str__

    def __getattr__(self, item):
        if item == 'hello':
            return 'world'
        elif item == 'age':
            return lambda x: x + 1
        else:
            raise AttributeError()

    def __call__(self):
        print('Hello world')


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            print(item.start, item.stop, item.step)
            return [1, 3, 4]


if __name__ == '__main__':
    s = Student('CCH')
    print(s)
    print(s.hello)
    print(s.age(10))
    print(callable(s))
    print(callable(True))
    s()

    print('*' * 40)
    for n in Fib():
        print(n)

    fib = Fib()
    print(fib[10])

    print(fib[2:4])
