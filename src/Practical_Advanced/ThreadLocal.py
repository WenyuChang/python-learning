__author__ = 'wenychan'

from time import sleep
from random import random
from threading import Thread, local

# One important thing that everybody seems to neglect
# to mention is that writing threadLocal = threading.local()
# at the global level is required. Calling threading.local()
# within the worker function will not work.
#
# Here is why: threading.local() actually creates an instance,
# a new one each time. This is necessary so that different modules
# do not conflict in their (potential) use of thread local storage.
# When attributes are accessed from the threadLocal variable
# (or whatever it is called), each thread gets its own view.
data = local()

def bar():
    print "I'm called from", data.v
    print

def foo():
    bar()

class T(Thread):
    def run(self):
        sleep(1)
        data.v = self.getName()   # Thread-1 and Thread-2 accordingly
        sleep(1)
        foo()

if __name__ == '__main__':
    T().start()
    T().start()