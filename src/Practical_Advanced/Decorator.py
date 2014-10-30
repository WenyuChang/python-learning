from functools import wraps


print ' Method Decorator '.center(60, '#')
def makebold(func):
    @wraps(func)
    def wrapped(printstr):
        return "<b>" + func(printstr) + "</b>"
    return wrapped

def makeunderline(func):
    @wraps(func)
    def wrapped(printstr):
        return "<u>" + func(printstr) + "</u>"
    return wrapped

def decorator_maker(arg1, arg2):
    def makeitalic(func):
        @wraps(func)
        def wrapped(printstr):
            return arg1+func(printstr)+arg2
        return wrapped
    return makeitalic
  
@decorator_maker("<i>", "</i>")
@makebold
@makeunderline
def hello(printstr):
    # If you are using decorators, be aware that wrapping a function with a decorator can
    # break the help features associated with documentation strings. For example, consider
    # this code:
    'this is hello'
    return printstr


print help(hello)
#print(hello("hello world"))


print ' Class Decorator '.center(60, '#')
def singleton_decorator(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton_decorator
class Singleton(object):
    pass

#=============================================================================

def logger(base_info):
    def sub_logger(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            print '{0} {1} is called with arguments - {2}, {3}'.format(base_info, func.__name__, args, kwargs)
            wrapped.__doc__ = func.__doc__
            wrapped.__name__ = func.__name__
            return func(*args, **kwargs)
        return wrapped
        sub_logger.__doc__ = wrapped.__doc__
        sub_logger.__name__ = wrapped.__name__
    return sub_logger

import datetime
@logger(str(datetime.time())+' --')
def hello1(string):
    'This is hello1'
    return string.upper()

print help(hello1)
print(hello1('wenychan'))