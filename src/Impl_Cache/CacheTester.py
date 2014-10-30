__author__ = 'wenychan'

import threading
import time
from Refresher import Refresher
from MyCache import MyCache
import sys
from CacheUnit import CacheUnit


def background_thread():
    class RefresherImpl1(Refresher):
        def refresh(self):
            return 'This is value needed cached'*1000

    refresher = RefresherImpl1()

    class RefresherImpl2(Refresher):
        def refresh(self):
            cache = MyCache()
            value = cache.retrieve('value1')
            return value

    refresher = RefresherImpl1()
    refresher2 = RefresherImpl2()



    cache = MyCache()
    cache.add_entry('value1', refresher, '5s')
    value = cache.retrieve('value1')

    time.sleep(1)

    cache.add_entry('value2', refresher2, '10s')
    value = cache.retrieve('value2')
    print value

    # value = cache.retrieve('value1')
    # time.sleep(1)
    #
    # cache.add_entry('value3', refresher, '20s')
    # value = cache.retrieve('value3')


    # cache.invalidate('value1')
    # cache.clear_cache_units()
    # time.sleep(6)
    #
    # cache = MyCache()
    # print cache
    # value = cache.retrieve('value1')
    # print value
    #
    #
    # cache = MyCache()
    # print cache
    # value = cache.retrieve('value2')
    # print value


if __name__ == '__main__':
    thread = threading.Thread(target=background_thread, name='Thread')
    thread.start()

    time.sleep(30)

    # class RefresherImpl1(Refresher):
    #     def refresh(self):
    #         return 'This is value needed cached'*10
    # refresher = RefresherImpl1()
    # unit = CacheUnit('aaa', refresher, '5s')
    # unit._CacheUnit__value = refresher.refresh()
    # print sys.getsizeof(unit)
    #
    # unit._CacheUnit__value = None
    # print sys.getsizeof(unit)
