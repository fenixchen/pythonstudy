# -*- coding:utf-8 -*-


import types


class Student(object):
    # only these attribute can be defined, not for child class
    __slots__ = ['name', 'age', 'set_age', 'score']


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


class Dog(object):
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 20:
            raise Exception('wrong age')
        self.__age = age


class Flyable(object):
    def fly(self):
        print("Flying")


class Runable(object):
    def run(self):
        print("Runing")


class Bat(Flyable, Runable):
    pass

if __name__ == '__main__':
    s = Student()
    # only for instance s
    s.name = 'CCH'
    print(s.name)
    s.set_age = types.MethodType(set_age, s)
    s.set_age(99)
    print(s.age)

    Student.set_score = set_score

    g = Student()
    g.set_score(38)
    s.set_score(100)
    # error
    # g.set_age(100)
    print('*' * 40)
    d = Dog(10)
    print(d.age)
    d.age = 19
    print(d.age)
    #d.age = 99

    print('*' * 40)
    b = Bat()
    b.fly()
    b.run()

