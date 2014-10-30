try:
    a=1
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print('Meet ZeroDivisionError...')
except:
    print('Meet other exception...')
else:
    print('No exception...')
    
#================================================

try:
    s = '12'
    if len(s) > 3:
        raise Exception()
except:
    print('raise a exception...')
else:
    print('No exception was raised.') 
finally:
    print('Ending...')
    
#================================================

class MyException(Exception):
    def __init__(self, name):
        self.str=name
    def __str__(self):
        return self.str
    
try:
    raise MyException('MyException-1')
# except MyException as ex:
except MyException as e:
    print(e)        