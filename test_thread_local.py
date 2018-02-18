# -*- coding:utf-8 -*-

import threading, time


local = threading.local()

def thread_func():
    print("thread %s" % threading.current_thread().name)
    local.i = 0
    for i in range(5):
        local.i = local.i + 1
        print('thread:%s, i:%d' % (threading.current_thread().name, local.i))
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_func, name='thread1')
    t2 = threading.Thread(target=thread_func, name='thread2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
