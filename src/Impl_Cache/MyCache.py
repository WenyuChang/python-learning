__author__ = 'wenychan'


import sys
import time
import operator
from SingletonType import SingletonType
from CacheUnit import CacheUnit
from threading import Timer


class MyCache(object):
    """ Impl_Cache module """
    from threading import Lock
    __metaclass__ = SingletonType
    __lock = Lock()

    def __init__(self, max_size=-1, size_check_interval=60*60):
        self.__cache_mgmt = {}
        self.__max_size = max_size
        self._size_check_interval = size_check_interval

        if self.__max_size > 0:
            from apscheduler.scheduler import Scheduler
            sched = Scheduler()
            sched.start()

            def __size_check():
                with self.__lock:
                    if sys.getsizeof(self) > self.__max_size:
                        temp_list = sorted(self.__cache_mgmt.values(), key=operator.attrgetter('last_access'))
                        if len(temp_list) > 0:
                            for unit in temp_list:
                                if unit.alive:
                                    print 'Reach max size. And invalidate cache unit ({0})'.format(unit.name)
                                    unit.invalidate(False)
                                    break

            sched.add_interval_job(__size_check, seconds=self._size_check_interval)

    def add_entry(self, name, refresher=None, expire=-1, retrieve=True):
        with self.__lock:
            if name in self.__cache_mgmt:
                print 'Impl_Cache {0} is already exist, cannot be add again...'.format(name)
            else:
                unit = CacheUnit(name, refresher, expire)
                self.__cache_mgmt[name] = unit

        if retrieve:
            self.retrieve(name)

    def retrieve(self, name):
        with self.__lock:
            if name is None or len(name) <= 0 or not name in self.__cache_mgmt:
                print 'Please provide the valid cache unit name...'
                return
            cache_unit = self.__cache_mgmt[name]

        print cache_unit.lock
        with cache_unit.lock:
            cache_unit.last_access = time.time()
            if cache_unit.alive:
                if cache_unit.expire > 0:
                    cache_unit.timer.cancel()
                    cache_unit.timer = None
            else:
                cache_unit.value = cache_unit.refresher.refresh()
                cache_unit.alive = True

            if cache_unit.expire > 0:
                cache_unit.timer = Timer(cache_unit.expire, cache_unit.invalidate)
                cache_unit.timer.daemon = True
                cache_unit.timer.start()
            return cache_unit.value

    def invalidate(self, name):
        with self.__lock:
            if name is None or len(name) <= 0 or not name in self.__cache_mgmt:
                print 'Please provide the valid cache unit name...'
                return
            cache_unit = self.__cache_mgmt[name]

        cache_unit.invalidate(False)

    def invalidate_all(self):
        with self.__lock:
            units = self.__cache_mgmt.values()
            for unit in units:
                unit.invalidate(False)

    def remove_cache_unit(self, name):
        with self.__lock:
            if name is None or len(name) <= 0 or not name in self.__cache_mgmt:
                print 'Please provide the valid cache unit name...'
                return

            cache_unit = self.__cache_mgmt[name]
            cache_unit.invalidate(False)
            del self.__cache_mgmt[name]

    def clear_cache_units(self):
        with self.__lock:
            for name, unit in self.__cache_mgmt.items():
                unit.invalidate(False)
                del self.__cache_mgmt[name]

    def __sizeof__(self):
        size = 0
        for key in self.__cache_mgmt.keys():
            unit = self.__cache_mgmt[key]
            size += sys.getsizeof(unit)
        return size