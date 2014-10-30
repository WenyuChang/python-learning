'''
Created on Mar 12, 2014

@author: wenychan
'''

class WithTarget():
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print 'enter ', self.name, '...'
        return 'This is return by __enter__'
    
    def __exit__(self,type,value,tb):
        '''If no exception has been raised,
           the three arguments to __exit__() are all set to None
        '''
        print 'exit ', self.name, '... '
        print 'type: ', type
        print 'value: ', value
        print 'traceback: ', tb
        
        return False

def withDemo():
    ins = WithTarget('with-target') 
    
    print 'Simple With Demo'.center(50, '=')
    with ins:
        for i in range(3):
            print 'In with (', i, ') ...'
            
    print 'With Demo (Has exception)'.center(50,'=')
    try:
        with ins:
            a = 1/0
            print a
    except:
        pass
    
    print 'With Demo (Has as)'.center(50,'=')
    with ins as str:
        print str
        
        
if __name__ == '__main__':
    withDemo()