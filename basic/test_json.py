# -*- coding:utf-8 -*-

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "(%s/%d/%d)" %(self.name, self.age, self.score)

def student2dict(s):
    return {'name': s.name,
            'age': s.age,
            'sc': s.score}

def dict2student(d):
    return Student(d['name'], d['age'], d['sc'])

if __name__ == '__main__':
    d = dict(name='cch', age=20, score=80)
    print(type(d))
    print(d)
    e = {'name': 'cch', 'age': 20, 'score': 80}
    print(type(e))
    print(e)
    print('*** dump')
    s = json.dumps(d)
    print(s)
    t = json.loads(s)
    print(t)

    print('*** student')
    s = Student('cch', 20, 90)
    t = json.dumps(s, default=student2dict)
    print(t)
    q = json.loads(t, object_hook=dict2student)
    print(q)

    print(json.dumps(s, default=lambda obj: obj.__dict__))
