'''
Created on Mar 12, 2014

@author: wenychan
'''

def typeDemo():
    # define a class Cls1
    class Cls1(object):
        def __init__(self):
            self.var = 1
    print Cls1
    print Cls1().var
    print Cls1.__dict__
    print Cls1().__dict__
    
    print '='*80
    
    # Another way of defining a class Cls2
    def __init__(self):
        self.var = -2
    Cls2 = type('Cls2', (object,), {'var':2, '__init__':__init__})
    print Cls2
    print Cls2.var
    print Cls2.__dict__
    print Cls2().__dict__

def typeDemo1():
    integer = 23
    print integer.__class__             # int
    print integer.__class__.__class__   # type

def metaClassDemo():
    class Cls1(object):
        pass
    
    from abc import ABCMeta
    class Cls2(object):
        __metaclass__ = ABCMeta
        
    print Cls1().__class__.__class__   # type
    print Cls2().__class__.__class__   # ABCMeta


def metaClassRealDemo():
    '''Imagine a stupid example, where you decide that all classes 
       in your module should have their attributes written in uppercase. 
       There are several ways to do this, but one way is to 
       set __metaclass__ at the module level.
    '''
    pass
    
    
if __name__ == '__main__':
    # typeDemo()
    
    # typeDemo1()
    
    metaClassDemo()