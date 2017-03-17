class A:
    pass


a = A()
a.aaa = 10
print a.aaa


if hasattr(a, 'bbb'):
    print a.bbb
else:
    print 'ccc'
