__author__ = 'wenychan'

from Refresher import Refresher
from threading import Lock
import sys
import time


def expire_parse(value):
    class ExpireTimeError(SyntaxError): pass
    if type(value) is int:
        return value
    elif type(value) is str:
        if value.isdigit():
            return int(value)
        else:
            import re
            prog = re.compile('[0-9]+(d|h|m|s|D|H|M|S)')
            if prog.match(value):
                unit = value[-1]
                if unit.lower() == 's':
                    return int(value[:-1])
                elif unit.lower() == 'm':
                    return int(value[:-1])*60
                elif unit.lower() == 'h':
                    return int(value[:-1])*60*60
                elif unit.lower() == 'd':
                    return int(value[:-1])*60*60*24
                else:
                    raise ExpireTimeError('Format is wrong for {0}'.format(value))
            else:
                raise ExpireTimeError('Format is wrong for {0}'.format(value))
    else:
        raise ExpireTimeError('Format is wrong for {0}'.format(value))


class CacheUnit(object):
    def __init__(self, name, refresher, expire=-1):
        # private variables
        self.__name = name
        self.__expire = expire_parse(expire)
        self.__value = None
        if isinstance(refresher, Refresher):
            self.__refresher = refresher
        else:
            raise AttributeError('Call back function mush be the sub-class of Refresh...')
        self.__alive = False
        self.__timer = None
        self.__last_access = time.time()
        self.__lock = Lock()

    @property
    def name(self):
        return self.__name

    @property
    def lock(self):
        return self.__lock

    @lock.setter
    def lock(self, lock):
        print 'Lock is final. Cannot be changed...'

    @property
    def expire(self):
        return self.__expire

    @expire.setter
    def expire(self, expire):
        print 'Expiration time is final. Cannot be changed...'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def refresher(self):
        return self.__refresher

    @refresher.setter
    def refresher(self, refresher):
        print 'Call back function is final. Cannot be changed...'

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, alive):
        self.__alive = alive

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, timer):
        self.__timer = timer

    @property
    def last_access(self):
        return self.__last_access

    @last_access.setter
    def last_access(self, now=time.time()):
        self.__last_access = now

    def invalidate(self, time_out=True):
        with self.lock:
            self.value = None
            self.timer.cancel()
            self.timer = None
            self.alive = False
            if time_out:
                print '{0} is timeout...'.format(self.__name)

    def __sizeof__(self):
        size = 0
        size += sys.getsizeof(type(self.__name)) + sys.getsizeof(self.__name)
        size += sys.getsizeof(type(self.__expire)) + sys.getsizeof(self.__expire)
        size += sys.getsizeof(type(self.__value)) + sys.getsizeof(self.__value)
        size += sys.getsizeof(type(self.__refresher)) + sys.getsizeof(self.__refresher)
        size += sys.getsizeof(type(self.__alive)) + sys.getsizeof(self.__alive)
        size += sys.getsizeof(type(self.__timer)) + sys.getsizeof(self.__timer)
        size += sys.getsizeof(type(self.__last_access)) + sys.getsizeof(self.__last_access)
        return size