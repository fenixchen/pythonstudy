# -*- coding:utf-8 -*-
from datetime import datetime, timedelta

if __name__ == '__main__':
    n = datetime.now()
    print(type(n))
    print(n)
    print(n.day)
    print(n.date())

    dt = datetime(2018, 1, 1)
    print(dt)
    print(dt.timestamp())  # sec.msec

    t = 1429417200.11
    print(datetime.fromtimestamp(t))

    print(datetime.utcfromtimestamp(t))

    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)

    now = datetime.now()
    next = now + timedelta(days = 1)
    print(now,',',next)