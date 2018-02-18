# -*- coding:utf-8 -*-

import base64

# length of base64 = 8bit * 3 / 4 * 6 = 36bit
if __name__ == '__main__':
    b = base64.b64encode(b'AAA')
    print(b)
    s = base64.b64decode(b)
    print(s)

    b = base64.urlsafe_b64encode(b'ABCDEFG')
    print(b)
    s = base64.urlsafe_b64decode(b)
    print(s)

