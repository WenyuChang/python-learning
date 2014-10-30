'''
Created on 20131220

@author: wenychan
'''

class Cls1(object):
    def func(self):
        print 'Cls1 func...'
        
    def _protect_func(self):
        # Attention: still can be seen outside the package
        print 'Cls1 protected func...'
        
class Cls2(object):
    def func(self):
        print 'Cls2 func...'

class ChildCls1(Cls1, Cls2):
    def func1(self):
        super(ChildCls1, self).func()
        
class ChildCls2(Cls2, Cls1):
    def func(self):
        super(ChildCls2, self).func()

class GrandChildCls1(ChildCls2, Cls2):
    '''ChildCls2 must be front of Cls2, or it will cause exception'''
    def func(self):
        pass

class Cls1WithoutImplObject:
    def func(self):
        print 'Cls1WithoutImplObject func...'

if __name__ == '__main__':
    ins1 = ChildCls1()
    ins1.func1()
    
    ins2 = ChildCls2()
    ins2.func()
    
    ins3 = Cls1WithoutImplObject()
    'type of ins1 is not type of ins3 just because Cls1 extends object'
    print type(ins1)  # <class '__main__.ChildCls1'>
    print type(ins3)  # <type 'instance'>