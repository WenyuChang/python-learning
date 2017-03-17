__author__ = 'wenychan'

from multiprocessing import Process, Queue, Pipe, Lock, Manager, Pool


def process_info(title):
    import os
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()


def func1(name):
    process_info('List process info')
    print 'hello', name


def func2(queue):
    queue.put('hello wenychan2')


def func4(l, i):
    l.acquire()
    print 'hello world', i
    l.release()


def func5(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


def func6(x):
    return x*x

def usage1():
    # simple demo with showing process message
    p1 = Process(target=func1, args=('wenychan1',))
    p1.daemon = False
    p1.start()
    p1.join()


def usage2():
    # Exchanging objects between processes
    q = Queue()
    p2 = Process(target=func2, args=(q, ))
    p2.start()
    print q.get()
    p2.join()


def usage3():
    # The Pipe() function returns a pair of connection objects
    # connected by a pipe which by default is duplex (two-way)
    parent_conn, child_conn = Pipe()
    child_conn.send('wenychan3')
    child_conn.close()
    print parent_conn.recv()   # prints "[42, None, 'hello']"


def usage4():
    # Synchronization between processes
    lock = Lock()
    for num in range(10):
        Process(target=func4, args=(lock, num)).start()


def usage5():
    # A manager object returned by Manager() controls a server process which holds
    # Python objects and allows other processes to manipulate them using proxies.
    # A manager returned by Manager() will support types list, dict, Namespace,
    # Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value and Array.
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=func5, args=(d, l))
    p.start()
    p.join()

    print d
    print l


def usage6():
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(func6, [10])    # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(func6, range(10))          # prints "[0, 1, 4,..., 81]"


if __name__ == '__main__':
    # usage1()

    # usage2()

    # usage3()

    # usage4()

    # usage5()

    usage6()