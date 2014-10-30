import sys

print('The command line arguments are:')
s=''
for i in sys.argv:
    s=s+' '+i
print(s)

#===============================================================

print('=================================================')
print('The PYTHONPATH is: ')
for path in sys.path:
    print(path)
    
print('api_version: ', sys.api_version)
print('base_exec_prefix: ', sys.base_exec_prefix)
print('builtin_module_names', sys.builtin_module_names)

#===============================================================

from sys import copyright
print(copyright)

#===============================================================

from sys import builtin_module_names as BMN
print(BMN)