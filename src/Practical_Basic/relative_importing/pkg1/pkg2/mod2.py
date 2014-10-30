__author__ = 'wenychan'

print 'Succeed to inport mod2.py in pkg2. Following is the package name of mod2:'
print "__name__ in mod2: ", __name__

def func():
    print 'This is func in mod2'

def func_call_mod1():
    print 'mod2 try to relative import mod in pkg1 by from .. import mod1'
    from .. import mod1
    mod1.func()