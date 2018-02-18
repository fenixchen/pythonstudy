# -*- coding:utf-8 -*-

import hashlib
import hmac

if __name__ == '__main__':
    md5 = hashlib.md5()
    md5.update('Hello'.encode('utf-8'))
    md5.update('world'.encode('utf-8'))
    print(md5.hexdigest())

    sha1 = hashlib.sha1()
    sha1.update('Hello'.encode('utf-8'))
    sha1.update('world'.encode('utf-8'))
    print(sha1.hexdigest())

    # add salt
    # use username as salt

    message = b'Hello world'
    key = b'salt'
    h = hmac.new(key, message, digestmod='MD5')
    h.update(b'AAA')
    print(h.hexdigest())
