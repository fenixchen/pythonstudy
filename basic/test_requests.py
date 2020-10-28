# -*- coding:utf-8 -*-

import requests

if __name__ == '__main__':
    '''
    r = requests.get('https://www.douban.com/')
    print(r.status_code)
    print(r.text)
    '''
    r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
    print(r.url)
    print(r.encoding)
    print(r.status_code)