class inputoutsrting(object):
    def __init__(self):
        self.s= "" 
    
    def getstring(self):
        self.s = input()

    def printstring(self):
        print(self.s.upper())


strobj = inputoutsrting()
strobj.getstring()
strobj.printstring()

