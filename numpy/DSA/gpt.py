class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def take_input(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an instance of the Person class
person1 = Person()

# Call the method to take input from the user
person1.take_input()

# Display the information
print(person1.display())
