__author__ = 'wenychan'


test_count = 1000

def simple_test(Singleton):
    for i in range(test_count):
        ins = Singleton()
        ins1 = Singleton()
        assert ins == ins1


def multi_thread_test(Singleton):
    import threading
    import sets
    import sys
    set = sets.Set()

    def func():
        ins = Singleton()
        set.add(ins)
        assert len(set) == 1

    for i in range(test_count):
        thread0 = threading.Thread(target=func, name='Thread0')
        thread1 = threading.Thread(target=func, name='Thread1')
        thread0.start()
        thread1.start()
        thread0.join()
        thread1.join()