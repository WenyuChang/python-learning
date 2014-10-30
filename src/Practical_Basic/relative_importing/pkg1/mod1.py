__author__ = 'wenychan'

print 'Succeed to inport mod1.py in pkg1. Following is the package name of mod1:'
print "__name__ in mod1: ", __name__

def func():
    print 'This is func in mod1'

    print 'mod1 try to relative import mod2 in pkg1.pkg2 by import pkg2.mod2'
    from pkg2 import mod2
    mod2.func()

def func_call_main():
    try:
        from .. import main
        main.func()
    except:
        print 'Failed to call main. since current package name is ', __name__, ', pkg1 is the top pageage name. so cannot import ".."'