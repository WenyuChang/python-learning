__author__ = 'wenychan'


class Clz(object):
    # instance final variable
    @property
    def final_variable(self):
        return 'final_instance_variable'

ins = Clz()
print ins.final_variable

try:
    ins.final_variable = 1
except AttributeError as error:
    print 'Try to set instance final variable, but got error: ', error
print ins.final_variable