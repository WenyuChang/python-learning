'''
Created on 20131220

@author: wenychan
'''

import Pyro4

uri = 'PYRO:obj_61baae0f76b5440eac8323c3090b0115@localhost:52035'
value = 'test'

ins = Pyro4.Proxy(uri)
print ins
print ins.print_func(value)
