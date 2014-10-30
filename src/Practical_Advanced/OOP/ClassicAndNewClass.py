'''
Created on 20131220

@author: wenychan
'''


class tt:
    pass


class tt1():
    pass


class tt2(object):
    pass


tt3 = type('tt3', (object,), {})
tt5 = type('tt5', (), {})


class tt6():
    __metaclass__ = type

ins_tt = tt()
ins_tt2 = tt2()

print ' classic class (before python 2.2) '.center(60, '#')
print 'type(tt): ', type(tt)
print 'type(tt1): ', type(tt1)
print 'type(ins_tt): ', type(ins_tt)
print 'ins_tt.__class__: ', ins_tt.__class__


print ' new class (after python 2.2) '.center(60, '#')
print 'type(tt2): ', type(tt2)
print 'type(tt3): ', type(tt3)
print 'type(tt5): ',  type(tt5)
print 'type(tt6): ',  type(tt6)
print 'type(ins_tt2): ', type(ins_tt2)
print 'ins_tt2.__class__: ', ins_tt2.__class__


