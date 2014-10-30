class FatherClass:
    clsVar=1
    def __init__(self):
        self.var1=1
        self.var2=2
        self.__privVar3=3
    def myFun(self):
        print('FatherClass call: ',FatherClass.clsVar,',',self.var1,',',self.var2,',',self.__privVar3)
    
fcls = FatherClass()
fcls.myFun()

class ChildClass(FatherClass):
    def __init__(self):
        FatherClass.__init__(self)
        self.var1='a'
        self.var2='b'
    def myFun(self):
        print('ChildClass call: ',FatherClass.clsVar,',',self.var1,',',self.var2)

chcls = ChildClass()
chcls.myFun()