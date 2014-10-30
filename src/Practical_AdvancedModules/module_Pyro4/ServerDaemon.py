'''
Created on 20131220

@author: wenychan
'''

import Pyro4


class Clz(object):
    def print_func(self, name):
        print 'Got request from client - ', name
        return 'Process request and print - ' + name

ins = Clz()
daemon = Pyro4.Daemon()
uri = daemon.register(ins)
print uri
daemon.requestLoop()
