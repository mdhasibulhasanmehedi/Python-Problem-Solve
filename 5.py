class sample:
    def __init__(self,s) :
        self.s=s                 

    def getstring(self):
        self.s=str(input())
    def  printstring(self):
        return self.s.upper()

obj=sample("")
obj.getstring()
print(obj.printstring())


