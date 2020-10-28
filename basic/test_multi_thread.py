# -*- coding:utf-8 -*-

import threading, time

lock = threading.Lock()


def loop():
    print('name:%s' % threading.current_thread().name)
    for i in range(5):
        lock.acquire()
        print("i:%d" % i)
        time.sleep(1)
        lock.release()
    print('name:%s end' % threading.current_thread().name)


if __name__ == '__main__':
    print('main:%s' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('main:%s join' % threading.current_thread().name)

    # Python cannot use multi cpu using multi thread
    # GIL (global Interpreter Lock)
    # use multi process instead
