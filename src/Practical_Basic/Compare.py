'''
Created on Mar 11, 2014

@author: wenychan
'''

def compare(a, b):
    if a is b:
        print 'a and b are the same object'
    if a == b:
        print 'a and b have the same value'
    if type(a) is type(b):
        print 'a and b have the same type'

if __name__ == '__main__':
    li1 = [1, 2, 3]
    li2 = [1, 2, 3]
    
    compare(li1, li2)
