'''
Created on Dec 28, 2013

@author: wenychan
'''

import soaplib
from soaplib.core.server import wsgi

from HelloWorldService import HelloWorldService
from ServiceWithoutReturn import PrintService
from ServiceWithModel import ModelService

if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        
        services = [HelloWorldService, PrintService, ModelService]
        
        soap_application = soaplib.core.Application(services, 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 7789, wsgi_application)
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"