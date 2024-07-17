#class to store and display information of student
class student:
    def __init__(self):
        self.name=""
        self.rollno=0
        self.marks=0

    def input(self):
        print("ENTER THE NAME")
        self.name=input()
        print("ENTER THE ROLLNO")
        self.rollno=int(input())
        print("ENTER THE MARKS")
        self.marks=int(input())

    def display(self):
        print("NAME",self.name)
        print("ROLLNO",self.rollno)
        print("MARKS",self.marks)

obj1=student()
obj1.input()
obj1.display()
obj2=student()  
obj2.input()
obj2.display()      

