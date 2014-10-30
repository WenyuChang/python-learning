__author__ = 'wenychan'


class TYPE_WITH_FINAL(type):
    class ConstError(TypeError): pass
    def __setattr__(cls, name, value):
        if name in cls.__dict__ and name.isupper():
            raise cls.ConstError, "Can't rebind const(%s)"%name
        else:
            super(TYPE_WITH_FINAL, cls).__setattr__(name,value)

class Clz(object):
    __metaclass__ = TYPE_WITH_FINAL
    STATIC_FINAL_VARIABLE = 'This is final static variable'

print Clz.STATIC_FINAL_VARIABLE
try:
    Clz.STATIC_FINAL_VARIABLE = 1
except Exception as ex:
    print 'Try to set instance final variable, but got error: ', ex
print Clz.STATIC_FINAL_VARIABLE

Clz.bbb = 1
Clz.bbb = 2
print Clz.bbb