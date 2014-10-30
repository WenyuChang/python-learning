'''
Created on Dec 25, 2013

@author: wenychan
'''

from soaplib.core.service import DefinitionBase, soap
from soaplib.core.model.primitive import String

class PrintService(DefinitionBase):
    @soap(String)
    def print_name(self,name):
        print "OtherService - printName: %s" % name 