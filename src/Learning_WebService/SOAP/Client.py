'''
Created on Dec 25, 2013

@author: wenychan
'''
from suds.client import Client

if __name__ == '__main__':
    client = Client("http://localhost:7789/?wsdl")
    print "#"*10, "\n", "Call say_hello:"
    print client.service.say_hello("Wenyu", 5)
     
    print "#"*10, "\n", "Call say_merryXMas:"
    print client.service.say_merryXMas("Wenyu", 5)
     
    print "#"*10, "\n", "Call print_name and print name in the server side"
    client.service.print_name("Wenyu")
      
    print "#"*10, "\n", "Call get_model"
    print client.service.get_model(1)