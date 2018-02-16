# -*- coding:utf-8 -*-

import unittest


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError('no attribute %s' % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_hello(self):
        self.assertTrue(2 == 2)

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.hello

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")



if __name__ == '__main__':
    unittest.main()
