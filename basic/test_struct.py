# -*- coding:utf-8 -*-

import struct
import binascii

if __name__ == '__main__':
    # convert to bytes
    # >: Big endian
    # I: unsigned int
    # H: unsigned short
    b = struct.pack('>II', 0x12345678, 0x87654321)
    print(type(b), '\t', b)
    print(binascii.hexlify(b))
    c = struct.unpack('>II', b)
    print('%x,%x' % (c[0], c[1]))

    b = b'\x11\x22\x33\x44\x55\x66'
    print(binascii.hexlify(b))
