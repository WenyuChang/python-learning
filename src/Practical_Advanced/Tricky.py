'''
Created on Mar 12, 2014

@author: wenychan
'''

def tricky1():
    a = 10
    def foo(x=a):
        return x
    
    a = 5 # Reassign 'a'.
    print foo()   # 10

def tricky2():
    def foo(x, items=[]):
        items.append(x)
        return items
    
    print foo(1) # returns [1]
    print foo(2) # returns [1, 2]
    print foo(3) # returns [1, 2, 3]
    
    
    def foo1(x, items=None):
        if items is None:
            items = []
        items.append(x)
        return items
    print foo1(1) # returns [1]
    print foo1(2) # returns [2]
    print foo1(3) # returns [3]
    
def tricky3():
    # function closures
    # which means that inner functions defined in non-global scope 
    # remember what their enclosing namespaces looked like at definition time
    def outer():
        x = 1
        def inner():
            print x
        return inner
    
    foo = outer()
    foo()  # 1
    
    def outer1(x):
        def inner():
            print x
        return inner
    
    foo = outer1(1)
    foo1 = outer1(2)
    foo()   #  1
    foo1()  #  2

if __name__ == '__main__':
    # tricky1()
    
    # tricky2()
    
    tricky3()