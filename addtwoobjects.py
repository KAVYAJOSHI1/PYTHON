#Python program toadd 2 numbers using two different objects
class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self):
        print("THE SUM OF TWO NUMBERS IS:")
        print(self.a+self.b)
obj1=add(10,20)
obj1.__add__()
