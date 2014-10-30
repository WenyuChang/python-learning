__author__ = 'wenychan'

def func(aa, bb, cc):
    print aa, bb, cc


def func1(*args, **kwargs):
    print args
    print kwargs


apply(func, ['aa', 'bb'], dict(cc='cc'))
apply(func1, ['aa', 'bb'], dict(cc=['cc']))