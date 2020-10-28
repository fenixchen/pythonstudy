# -*- coding:utf-8 -*-

import pickle
import os

if __name__ == '__main__':
    d = {'name':'CCH', 'age': 40}
    print(d)
    s = pickle.dumps(d)
    print(s)

    print('**** load')
    with open('./hello.txt', 'wb') as f:
        pickle.dump(d, f)

    with open('./hello.txt', 'rb') as f:
        e = pickle.load(f)
        print(e)
    print(pickle.loads(s))
    os.remove('./hello.txt')