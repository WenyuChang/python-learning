'''
Created on Feb 24, 2014

@author: wenychan
'''

# thread is because there is no control of when
# your process exits. When the main thread finishes, any other threads will also
# die, without warning or proper cleanup. As mentioned earlier, at least threading
# allows the important child threads to finish first before exiting.

def simpleDemo(): 
    import time
    import thread
    def loop0():
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
    def loop1():
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()
        
    print 'starting at:', time.ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    
    # The reason is that if we did not stop
    # the main thread from continuing, it would proceed to the next statement,
    # displaying "all done" and exit, killing both threads running loop0() and
    # loop1().
    time.sleep(6)
    # time.sleep(2)
    print 'all DONE at:', time.ctime()
    
def demoWithLock():
    import time
    import thread
    def loop0(lock):
        print 'start loop0 at:', time.ctime()
        time.sleep(4)
        print 'loop0 done at:', time.ctime()
        lock.release()
    def loop1(lock):
        print 'start loop1 at:', time.ctime()
        time.sleep(2)
        print 'loop1 done at:', time.ctime()
        lock.release()
    
    lock0 = thread.allocate_lock()
    lock0.acquire()
    lock1 = thread.allocate_lock()
    lock1.acquire()
    
    thread.start_new_thread(loop0, (lock0,))
    thread.start_new_thread(loop1, (lock1,))
    
    while lock0.locked(): pass
    while lock1.locked(): pass
    
    print 'all DONE at:', time.ctime()  


def threadLocalDemo():
    pass

if __name__ == '__main__':
    # simpleDemo()
    demoWithLock()