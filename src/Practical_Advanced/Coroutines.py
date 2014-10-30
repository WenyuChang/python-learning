'''
Created on Mar 11, 2014

@author: wenychan
'''

def print_matches(matchtext):
    print "Looking for", matchtext
    while True:
        line = (yield)  # Get a line of text
        if matchtext in line:
            print line

def commandConsoleDemo():
    def coroutine(func):
        def wrapped(*args,**kwargs):
            g = func(*args,**kwargs)
            g.next()
            return g
        return wrapped
    
    @coroutine
    def commandParse():
        while True:
            commond = (yield)
            print 'Type-in commond: ', commond
            
    import sys
    cp = commandParse()
    while True:
        print 'Input commond: '
        command = sys.stdin.readline()
        if not command:
            break
        command = command.strip()
        cp.send(command)
        if command == 'exit':
            cp.close()
            break            

if __name__ == '__main__':
    '''Usage:
        >>> matcher = print_matches("python")
        >>> matcher.next() # Advance to the first (yield)
        Looking for python
        >>> matcher.send("Hello World")
        >>> matcher.send("python is cool")
        python is cool
        >>> matcher.send("yow!")
        >>> matcher.close() # Done with the matcher function call
    '''
    commandConsoleDemo()