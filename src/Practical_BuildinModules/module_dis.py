__author__ = 'wenychan'

import dis

def simple_func():
    print 'This is simple func...'
    return 'This is simple func...'

def func(*args):
    for arg in args:
        print arg;


dis.dis(simple_func())

# dis.dis(func(1, 2, 3))