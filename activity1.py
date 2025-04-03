class IOString:
    def __init__(self):
        self.str1=''
    def strinput(self):
        self.str1=input("enter the letter : ")
    def opstring(self):
        print('uppercase of',self.str1.upper())
    def __del__(self):
        print("Object destroyed")

obj=IOString()
obj.strinput()
obj.opstring()
del obj
