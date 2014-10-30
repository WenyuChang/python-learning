'''
Created on Feb 24, 2014

@author: wenychan
'''

# Create Thread instance, passing in function
# Create Thread instance, passing in callable class instance
# Subclass Thread and create subclass instance

def demoPassinFunc():
    import time
    import threading
    def loop0():
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
    def loop1():
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()
    
    # 
    thread0 = threading.Thread(target=loop0, name='Thread0')
    thread1 = threading.Thread(target=loop1, name='Thread1')
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  
    

def demoPassinCallableIns():
    import time
    import threading
    class ThreadCallable(object):
        def __init__(self, func, args=(), name=''):
            self.name = name
            self.func = func
            self.args = args
            
        def __call__(self):
            self.func(*self.args)
            
    def loop0():
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
    def loop1():
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()

    thread0 = threading.Thread(target=ThreadCallable(loop0, name=loop0.__name__))
    thread1 = threading.Thread(target=ThreadCallable(loop1, name=loop1.__name__))
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  

def demoImplThread():
    import time
    import threading
    class MyThread(threading.Thread):
        def __init__(self, func, args=(), name=''):
            threading.Thread.__init__(self)
            self.name = name
            self.func = func
            self.args = args
            
        def run(self):
            self.func(*self.args)
            
    def loop0():
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
    def loop1():
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()

    thread0 = MyThread(loop0, name=loop0.__name__)
    thread1 = MyThread(loop1, name=loop1.__name__)
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  

def demoWithLock():
    import time
    import threading
    def loop0():
        lock.acquire()
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
        lock.release()
    def loop1():
        lock.acquire()
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()
        lock.release()
    
    lock = threading.Lock()
    thread0 = threading.Thread(target=loop0, name='Thread0')
    thread1 = threading.Thread(target=loop1, name='Thread1')
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  
    
def demoWithRLock():
    # RLock is a reentrant lock. acquire() can be called 
    # multiple times by the same thread without blocking. 
    # Keep in mind that release() needs to be called the 
    # same number of times to unlock the resource.
    import time
    import threading
    def loop0():
        lock.acquire()
        lock.acquire()
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
        lock.release()
        lock.release()
    def loop1():
        lock.acquire()
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()
        lock.release()
    
    lock = threading.RLock()
    thread0 = threading.Thread(target=loop0, name='Thread0')
    thread1 = threading.Thread(target=loop1, name='Thread1')
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  

def demoWithCondition():
    import time
    import threading
    def loop0():
        condition.acquire()
        print 'start loop0 at:', time.ctime()
        condition.wait()
        print 'loop0 done at:', time.ctime()
        condition.release()
    def loop1():
        condition.acquire()
        print 'start loop1 at:', time.ctime(), 'loop0 is waiting... and is going to be notified by loop1.'
        condition.notify()
        print 'loop1 done at:', time.ctime()
        condition.release()
    
    condition = threading.Condition()
    thread0 = threading.Thread(target=loop0, name='Thread0')
    thread1 = threading.Thread(target=loop1, name='Thread1')
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  
    
    
def demoWithSemaphore():
    import time
    import threading
    def loop0():
        semaphore.acquire()
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
        semaphore.release()
    def loop1():
        semaphore.acquire()
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()
        semaphore.release()
    
    semaphore = threading.Semaphore(1) # only one thread can be run at any given time
    # semaphore = threading.Semaphore(2) # only two threads can be run at any given time
    thread0 = threading.Thread(target=loop0, name='Thread0')
    thread1 = threading.Thread(target=loop1, name='Thread1')
    
    thread0.start()
    thread1.start()
    
    # these joins can make sure the print statement will be executed 
    # after both thread finish.
    thread0.join()
    thread1.join()
    print 'all DONE at:', time.ctime()  
    
if __name__ == '__main__':
    # demoPassinFunc()
    # demoPassinCallableIns()
    # demoImplThread()
    # demoWithLock()
    # demoWithRLock()
    # demoWithCondition()
    demoWithSemaphore()