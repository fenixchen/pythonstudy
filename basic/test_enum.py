# -*- coding:utf-8 -*-

from enum import Enum, unique

Week = Enum('Week', ('Mon', 'Tue', 'Wed'))


@unique
class Weekday(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4


if __name__ == '__main__':
    for name, member in Week.__members__.items():
        print(name, '=>', member)


    day1 = Weekday.Mon
    print(type(day1))
    print(day1)
    print(day1.value)
    print(Weekday(2))