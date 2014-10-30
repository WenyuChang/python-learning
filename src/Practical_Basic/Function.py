def myFun():
    print('this is a function.')

myFun()    

#===========================================================
#Demo of function with argument
 
def myFun1(i):
    print('this is a function with one argument:', i)
    
myFun1('argument')
myFun1(1)
myFun1(3+5j)
myFun1(True)

#===========================================================
#Demo of value-pass of function

def myFun2(a,b):
    c=a
    a=b
    b=c
    print(a,b)

a=1
b=2
x=50
myFun2(a,b)
print(a,b)

#===========================================================
#Demo of global argument

def myFun3():
    global c
    x=30
    print('inside myFun3: x=',x)

myFun3()
print('outside myFun3: x=',x)

#===========================================================
#Demo of default value of argument

def myFun4(a,b=3,c=10,d=30):
    print(a,',',b,',',c,',',d)
    
myFun4(1,2,3,4)
myFun4(1,2,3)
myFun4(1,2)
myFun4(1)

#===========================================================
#Demo of keyword argument

def myFun5(a,b=1,c=2,d=3):
    print(a,',',b,',',c,',',d)
    
myFun5(1,2)
myFun5(c=1,a=3,b=6)
myFun5(a=1)

#===========================================================
#Demo of function with return

def myFun6(a,b):
    if a>b:
        return 'a>b'
    elif a<b:
        return 'b<a'
    else:
        return 'same'

print('Result:', myFun6(1,2))
print('Result:', myFun6(2,1))
print('Result:', myFun6(1,1))

#===========================================================
#Demo of docString in function

def myFun7(a,b):
    '''This is an function will plus arguments, return result'''
    return a+b

print('Sum:', myFun7(3,5))
print('Sum:', myFun7('a','b'))
print(myFun7.__doc__)
help(myFun7)

#===========================================================
#Demo of mutable variables in function

def myFun8(a,*argv):
    s=a
    print(argv)
    for i in argv:
        s+=i
    print('total is:',s)

myFun8(1,2,3,4,5,6,7,8,9,10)
myFun8('a','b','c','d','e')

#===========================================================
#Demo of dictionary variables in function

def myFun9(a,**dic):
    print('a:',a)
    for key,value in dic.items():
        print('%s:%s' % (key,value))
        
myFun9(1, key1='value1', key2='value2')
