''' Dir function will return all the properties and function of module'''
import sys

prop1=1
prop2=2
prop3='a'
prop4='b'
prop5=True

def myFun():
    print('My function...')

#=======================================================================

s='All the props and funs of Sys: \n'
for i in dir(sys):
    s+=i+', '
print(s)

#=======================================================================

s='\nAll the props and funs of this module: \n'
for i in dir():
    s+=i+', '
print(s)

#=======================================================================

del prop5
s='\nAll the props and funs of this module after delete prop5: \n'
for i in dir():
    s+=i+', '
print(s)
    
