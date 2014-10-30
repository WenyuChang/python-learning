'''
Created on Mar 11, 2014

@author: wenychan
'''

# must manually add (object) here. Reason: super in ChildClass3
class ParentClass(object):
    # static variables
    public_static_var = 1
    _protected_static_var = 2 # cannot be seen "from ParentClass import *"
    __private_static_var = 3
    var = 23 # different from self.var which is -23
    
    def __init__(self):
        print 'ParentClass __init__'
        self.public_var = 4
        self._protected_var = 5
        self.__private_var = 6
        self.var = -23
        
    def public_func(self):
        return 'This is a public instance function...'
    
    def __private_func(self):
        return 'This is a private instance function...'
    
    def _func(self):
        return 'Call private class: '+self.__private_func()
    
    @staticmethod
    def public_static_func():
        return 'This is a public class function...'
    
    @staticmethod
    def __private_static_func():
        return 'This is a private class function...'


class ChildClass1(ParentClass):
    pass

class ChildClass2(ParentClass):
    def __init__(self):
        self.public_var1 = -4
        
class ChildClass3(ParentClass):
    def __init__(self):
        super(ChildClass3, self).__init__()
        
class ChildClass4(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)

def childClassDemo():
    ins1 = ChildClass1()
    print 'call ChildClass1 instance variable'.center(90, '=')
    print 'ins1.public_var:', ins1.public_var    # 4
    print 'ins1._protected_var: ', ins1._protected_var               # 5
    try:
        print 'ins1.__private_var: ', ins1.__private_var
    except:
        print 'Meet exception when call ins.__private_var, since it cannot inherit private variable from parent.'
        
    ins2 = ChildClass2()
    print 'call ChildClass2 instance variable'.center(90, '=')
    print 'ins2.public_var1:', ins2.public_var1    # -4
    try:
        print 'ins2.public_var2: ', ins2.public_var
    except:
        print 'Meet exception when call ins2.public_var2, since ChildClass2 has __init__, it doesnt have such variable'
    
    
    ins3 = ChildClass3()
    print 'call ChildClass3 instance variable'.center(90, '=')
    print 'ins3.public_var:', ins3.public_var    # 4
    
    ins4 = ChildClass4()
    print 'call ChildClass4 instance variable'.center(90, '=')
    print 'ins4.public_var:', ins4.public_var    # 4

def parentClassDemo():
    # create instances of ParentClass
    ins = ParentClass()
    
    
    print 'call instance variable'.center(90, '=')
    print 'ins.public_var:', ins.public_var    # 4
    print 'ins._protected_var: ', ins._protected_var               # 5
    try:
        print 'ins.__private_var: ', ins.__private_var
    except:
        print 'Meet exception when call ins.__private_var, since it is private.'
    
    
    #=================================================================================
    print
    print 'call class variable'.center(90, '=')
    print 'ins.public_static_var: ', ins.public_static_var      # 1
    print 'ParentClass.public_static_var: ', ParentClass.public_static_var      # 1
    print 'ins._protected_static_var: ', ins._protected_static_var  # 2
    print 'ParentClass._protected_static_var: ', ParentClass._protected_static_var   # 2
    try:
        print 'ParentClass.__private_static_var: ', ParentClass.__private_static_var
    except:
        print 'Meet exception when call ParentClass.__private_static_var, since it is private.'
    print 'ins.var: ', ins.var   # -23
    print 'ParentClass.var: ', ParentClass.var   # 23


    #=================================================================================
    print
    print 'call instance method'.center(90, '=')
    print 'ins.public_func: ', ins.public_func()   # This is a public instance function...
    print 'ins._func: ', ins._func()
    try:
        ins.__private_func()
    except:
        print 'Meet exception when call ins.__private_func(), since this function is private.'
    try:
        ParentClass.public_func()
    except:
        print 'Meet exception when call ParentClass.public_func(), since try call an instance function with Class.'
    print 'ParentClass.public_func(ins): ', ParentClass.public_func(ins)
    
    
    #=================================================================================
    print
    print 'call class method'.center(90, '=')
    print 'ParentClass.public_static_func:', ParentClass.public_static_func()  # This is a public class function...
    try:
        ParentClass.__private_static_func()
    except:
        print 'Meet exception when call ParentClass.__private_static_func(), since this function is private.'


if __name__ == '__main__':
    # parentClassDemo()
    childClassDemo()