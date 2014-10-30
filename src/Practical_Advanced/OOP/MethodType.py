'''
Created on Mar 11, 2014

@author: wenychan
'''

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)" % (self,x)

    @classmethod
    def class_foo(cls,x):
        ''' you can also call class_foo using the class. 
            In fact, if you define something to be a classmethod, 
            it is probably because you intend to call it from the 
            class rather than from a class instance. 
            
            A.foo(1) would have raised a TypeError, 
            but A.class_foo(1) works just fine:
        '''
        print "executing class_foo(%s,%s)" % (cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x

if __name__ == '__main__':
    ins = A()
    
    # instance method
    ins.foo(1)
    A.foo(ins,1)
    
    # class method
    A.class_foo(1)
    ins.class_foo(1)
    
    # static method
    ins.static_foo(1)
    A.static_foo(1)