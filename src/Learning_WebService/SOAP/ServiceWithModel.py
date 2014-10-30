'''
Created on Dec 28, 2013

@author: wenychan
'''

from soaplib.core.service import soap, DefinitionBase
from soaplib.core.model.clazz import ClassModel
from soaplib.core.model.primitive import Integer, String
 
class MyModel(ClassModel):
    modelId = String
    name = String
     
#     def __init__(self, modelId, name):
#         self.modelId = modelId
#         self.name = name
     
    def __str__(self):
        return 'MyModel(%s) - %s' %(self.modelId, self.name) 
 
class ModelService(DefinitionBase):
     
    @soap(Integer, _returns=MyModel)
    def get_model(self, modelId):
        import uuid
        name = str(uuid.uuid4()).upper().replace('-', '')
        model = MyModel(modelId, name)
        return model
     
    @soap(MyModel, _returns=String)
    def set_model(self, model):
        print "Set Model: "
        return model