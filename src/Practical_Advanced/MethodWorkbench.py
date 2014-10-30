__author__ = 'wenychan'

def workbench(func):
    import time
    def wrapped(*args, **kwargs):
        start_time = time.time()
        return_value = func(*args, **kwargs)
        end_time = time.time()
        print '{0} costs {1}'.format(func.__name__, end_time-start_time)
    return wrapped

@workbench
def func(passin):
    print 'This is {0}'.format(passin)
    for i in range(100000):
        pass


if __name__ == '__main__':
    func('test')