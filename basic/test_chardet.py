# -*- coding:utf-8 -*-

import chardet

if __name__ == '__main__':
    print(chardet.detect(b'Hello world'))
    b = '你好'.encode('utf-8')
    print(chardet.detect(b))
    b = '你好中国'.encode('gbk')
    print(chardet.detect(b))