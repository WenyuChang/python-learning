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


if __name__ == '__main__':
    countDownDemo(5)