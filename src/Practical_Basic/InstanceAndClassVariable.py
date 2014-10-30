'''
Created on Jan 4, 2014

@author: wenychan
'''

class MyClass:
    classVar = 'This is Class Variable.'
    x = 'This is Class Variable X'
    a = 'This is Class Variable A'
    def __init__(self, var, x):
        self.insVar = var
        self.x = x
    

if __name__ == '__main__':
    ins1 = MyClass('This is ins1 variable', 'This is ins1 variable X')
    ins2 = MyClass('This is ins2 variable', 'This is ins2 variable X')

    print 'Ins1.classVar: ', ins1.classVar # Ins1.classVar:  This is Class Variable.
    print 'Ins2.classVar: ', ins2.classVar # Ins2.classVar:  This is Class Variable.
    print 'MyClass.classVar: ', MyClass.classVar # Ins2.classVar:  This is Class Variable.
    
    print 'Ins1.insVar: ', ins1.insVar # Ins1.insVar:  This is ins1 variable
    print 'Ins2.insVar: ', ins2.insVar # Ins2.insVar:  This is ins2 variable
    
    print 'Ins1.x: ', ins1.x # Ins1.x:  This is ins1 variable X
    print 'Ins2.x: ', ins2.x # Ins2.x:  This is ins2 variable X
    print 'MyClass.x: ', MyClass.x # MyClass.x:  This is Class Variable X
    
    print 'MyClass.a: ', MyClass.a # MyClass.a:  This is Class Variable A
    print 'ins1.a: ', ins1.a # ins1.a:  This is Class Variable A
    MyClass.x = 'This is Class Variable Y'
    ins1.a = 'This is instance Variable A' # Note: python will create an instance var named a
    MyClass.a = 'This is Class Variable C'
    print 'MyClass.x: ', MyClass.x # MyClass.x:  This is Class Variable Y
    print 'MyClass.a: ', MyClass.a # MyClass.a:  This is Class Variable C
    print 'ins1.a: ', ins1.a # ins1.a:  This is instance Variable A
    print 'ins2.a: ', ins2.a # ins2.a:  This is Class Variable C
    pass