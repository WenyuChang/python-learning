'''
Created on Mar 11, 2014

@author: wenychan
'''

class Abstract:
    def func1(self):
        raise NotImplementedError('The method not implemented')

class Implement(Abstract):
    def func1(self):
        print 'func1 is implemented...'


from abc import ABCMeta, abstractmethod, abstractproperty
class Abstract1:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def func1(self):
        pass
    @abstractproperty
    def var(self):
        pass
    @abstractmethod
    def func3(self):
        pass
    
    def func2(self):
        print 'this is func2'
        
    

class Implement1(Abstract1):
    def func1(self):
        print 'this is func1 from implement1...'
        
    def var(self):
        return 'this is var from implement1...'
    
    def func3(self, name):
        print 'this is func3 from implement1...', name, '(abc module dont check arguments of func)'

if __name__ == '__main__':
#     ins = Implement()
#     ins.func1()

    ins = Implement1()
    ins.func1()
    ins.func2()
    ins.func3('name')