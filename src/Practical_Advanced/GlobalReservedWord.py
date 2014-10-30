'''
Created on Mar 11, 2014

@author: wenychan
'''

globvar = 0
globvar1 = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print 'globvar:', globvar     # No need for global declaration to read value of globvar
    print 'globvar1: ', globvar1


if __name__ == '__main__':
    set_globvar_to_one()
    print_globvar()       # Prints 1