'''
Created on Dec 25, 2013

@author: wenychan
'''

import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array


class HelloWorldService(DefinitionBase):
    @soap(String,Integer,_returns=Array(String))
    def say_hello(self,name,times):
        results = []
        for i in range(0,times):
            results.append('Hello, %s'%name)
        return results
    
    @soap(String,Integer,_returns=Array(String))
    def say_merryXMas(self,name,times):
        results = []
        for i in range(0,times):
            results.append('Merry XMas, %s'%name)
        return results