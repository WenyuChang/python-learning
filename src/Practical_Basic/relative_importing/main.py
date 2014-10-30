__author__ = 'wenychan'

def func():
    print 'func in main'


from pkg1 import mod1
# output:
#   Succeed to inport mod1.py in pkg1. Following is the package name of mod1:
#   __name__ in mod1:  pkg1.mod1


mod1.func()
# output:
#     This is func in mod1
#     mod1 try to relative import mod2 in pkg1.pkg2 by import pkg2.mod2
#     Succeed to inport mod2.py in pkg2. Following is the package name of mod2:
#     __name__ in mod2:  pkg1.pkg2.mod2
#     This is func in mod2



#
#
#
# mod1.func_call_main()
#
#
# from pkg1.pkg2.mod2 import func_call_mod1
# func_call_mod1()