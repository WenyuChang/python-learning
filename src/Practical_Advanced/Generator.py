'''
Created on Mar 11, 2014

@author: wenychan
'''

def countDownDemo(n):
    def countdown(n):
        print "Counting down!"
        while n > 0:
            yield n # Generate a value (n)
            n -= 1
            
    for n in countdown(n):
        print n,

def countDownDemo1(n):
    def countdown(n):
        print "Counting down!"
        while n > 0:
            yield n # Generate a value (n)
            n -= 1

    while(True):
        print next(countdown(n))

def tailDemo(f):
    def tail(f):
        import time
        f.seek(0,2) # Move to EOF
        while True:
            line = f.readline() # Try reading a new line of text
            if not line: # If nothing, sleep briefly and try again
                time.sleep(0.1)
                continue
            yield line
    
    for line in tail(f):
        print line


def iterDemo():
    class TestCls:
        cc = 'cc'
        dd = 'dd'

        def __init__(self):
            self.aa = 'aa'
            self.bb = 'bb'
            self.li = [self.aa, self.bb, self.cc, self.dd]


        def func(self):
            for item in self:
                print item

        def __iter__(self):
            """
            Iterator used to iterate thru the list
            """
            for item in self.li:
                yield item  # returning the next item

    aa = TestCls()
    aa.func()


if __name__ == '__main__':
    countDownDemo(5)

    print
    print '#'*60

    countDownDemo1(5)
    # iterDemo()