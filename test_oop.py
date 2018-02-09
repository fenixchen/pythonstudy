# -*- coding:utf-8 -*-
import types


# inherit from object
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__gender = True

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


class Animal(object):
    world = "Hello world"

    def run(self):
        print("Animal run")


class Dog(Animal):
    def run(self):
        print("Dog run")

    def __len__(self):
        return 100


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    s = Student('CCH', 65)
    s.print_score()
    print(s.get_grade())
    s.age = 100

    print(s, s.age)
    print(Student)

    print(dir(s))
    print(s._Student__gender)
    # error, cannot access private
    # print(s.__gender)

    animal = Animal()
    dog = Dog()
    run_twice(animal)
    run_twice(dog)

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(isinstance(animal, Dog))

    print(type(dog))

    print(type(run_twice))
    print(types.FunctionType)

    f = lambda x: x * x
    print(type(f))
    print(types.LambdaType)
    print(isinstance(f, types.LambdaType))

    l = [x for x in range(2, 9)]
    print(l, l.__len__())

    print(len(dog))

    print('*' * 40)
    print(hasattr(dog, 'run'))
    print(hasattr(dog, 'run1'))
    f = getattr(dog, 'run')
    print(f)
    f()

    print(type(dog.world))