'''
Created on Mar 11, 2014

@author: wenychan
'''

def func():
    'nonlocal reserved word only supported in Python 3'
    
    var1 = 1
    var2 = 2
    
    def sub_func():
        var1 = 2
        # nonlocal var2
        # var2 = 4
        
        print 'var1 in sub_func: ', var1   # 2
        print 'var2 in sub_func: ', var2   # 4
    
    print 'var1 in func: ', var1   # 1
    print 'var2 in func: ', var2   # 4


if __name__ == '__main__':
    func()