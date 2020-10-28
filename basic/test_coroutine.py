# -*- coding:utf-8 -*-
def consumer():
    print("consumer in")
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    print("produce in")
    c.send(None)
    print("produce send none")
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
