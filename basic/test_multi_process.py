# -*- coding:utf-8 -*-
import os
import time
import random
import subprocess

from multiprocessing import Process, Pool, Queue


def run_proc(arg):
    print('arg:%s, pid:%d/%d' % (arg, os.getpid(), os.getppid()))
    time.sleep(3)
    print('arg:%s, pid:%d/%d exit' % (arg, os.getpid(), os.getppid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':

    print('<<Process Communication>>', '*' * 40)
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


    print('<<SubProcess>>', '*' * 40)
    CMD = 'netsh'
    print(CMD)
    INPUT = b'?\r\nquit\r\n'
    p = subprocess.Popen([CMD], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(INPUT)
    print(output.decode('gbk'), p.returncode)

    print('pid:%s' % os.getpid())
    print('<<fork>>', '*' * 40)
    if os.name != 'nt':
        pid = os.fork()
        if pid == 0:
            print('child %d ppid %d' % (os.getpid(), os.getppid()))
        else:
            print('me %d ppid %d' % (os.getpid(), os.getppid()))
    else:
        print('windows cannot fork()')

    print('<<Process>>', '*' * 40)
    p = Process(target=run_proc, args=('child',))
    print('start child')
    p.start()
    p.join()
    print('child exit')

    print('<<Pool>>', '*' * 40)
    p = Pool(4)
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))

    print('waiting all')
    p.close()
    p.join()
    print('waiting done')
