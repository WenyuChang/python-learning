class MyClass:
    # followings are class variables
    classA=1
    classB=2
    classC=3
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.__privateA=1 # private (name mangling during runtime)
        self._privateA=2 # obey python coding convention, consider it as private, it can be accessed by outside, but not suggest
        print('initializing class...')
        
    def __del__(self):
        print('del instance...')
        
    def printAB(self):
        print(self.a,',',self.b,',',self.c)
        
    def printABC(self):
        self.c=3
        print(self.a,',',self.b,',',self.c)
        
    def printClassABCD(self):
        MyClass.classA=2
        MyClass.classD=4
        print(MyClass.classA,',',MyClass.classB,',',MyClass.classC,',',MyClass.classD)
    def __printClassName(self):
        print('the name of this class is MyClass...')
    
    def __str__(self):
        ''' like toString() '''
        return 'call __str__'
    def __len__(self):
        ''' will be called when using len(), must return an integer'''
        return 9999999
    def __repr__(self):
        return 'call __depr__'

cls = MyClass(1,2)
cls.printABC()
cls.printAB()
cls.printClassABCD()
cls.d=5
print(cls.d)
print('_privateA:',cls._privateA)
print('__privateA:',cls._MyClass__privateA)
cls._MyClass__printClassName()

cls1 = MyClass('a','b')
cls1.printABC()
cls1.printAB()
cls1.printClassABCD()

print(cls)
print('len:',len(cls))
print('repr:',repr(cls))
print('str:',str(cls))