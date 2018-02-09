# -*- coding:utf-8 -*-


import sys

if __name__ == '__main__':
    from submodule.test import test_func

    test_func()

    import submodule.test

    submodule.test.test_func()

    print('\n'.join(sys.path))

    # change environment variable PYTHONPATH
    sys.path.append('e:\\')
    print('\n'.join(sys.path))
