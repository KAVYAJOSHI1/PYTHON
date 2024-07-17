"""Create a class called `Book` that has the following features:

1. **Attributes**:
    - `title` (string)
    - `author` (string)
    - `price` (float)
    - `copies` (integer)

2. **Methods**:
    - `__init__`: Initializes the `title`, `author`, `price`, and `copies` attributes.
    - `take_input`: Prompts the user to enter the book's title, author, price, and number of copies.
    - `display`: Prints the book's details including title, author, price, and number of copies.
    - `sell_copies`: Prompts the user to enter the number of copies to sell. If the number of copies to sell is less than or equal to the available copies, update the number of copies and print the total price. Otherwise, print a message indicating insufficient copies.

Example Interaction:

Enter book title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter price: 10.99
Enter number of copies: 100

"""
class Book:
    def __init__(self):
        self.title=""
        self.author=""
        self.price=0
        self.copies=0

    def input(self):
        print("ENTER BOOK NAME")
        self.title=input()
        print("ENTER AUTHOR NAME")
        self.author=input()
        print("ENTER BOOK PRICE")
        self.price=int(input())
        print("ENTER NUMBER OF COPIES")
        self.copies=int(input())

    def display(self):
        print("BOOK NAME: "+self.title)
        print("AUTHOR NAME: "+self.author)
        print("BOOK PRICE: "+str(self.price))
        print("NUMBER OF COPIES: "+str(self.copies))

    def sell_copies(self):
        print("ENTER THE NUMBER OF COPIES TO SELL")
        sell=int(input()) 
        if sell<=self.copies:
            self.copies=self.copies-sell
            print("TOTAL PRICE: "+str(sell*self.price))
        else:
            print("INSUFFICIENT COPIES")

obj=Book()
obj.input()
obj.display()
obj.sell_copies()                   
