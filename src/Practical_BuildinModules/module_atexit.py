__author__ = 'wenychan'

import atexit
# This module is a straightforward wrapper for the sys.exitfunc hook.


def my_exit_hook_func(*args):
    print "exit", args

# register three exit handlers
atexit.register(my_exit_hook_func)
atexit.register(my_exit_hook_func, 1)
atexit.register(my_exit_hook_func, "hello", "world")

if __name__ == '__main__':
    print 'module running...'