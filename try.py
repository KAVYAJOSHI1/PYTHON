import sqlite3

class Book:
    def __init__(self):
        self.connection = sqlite3.connect('books.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                price REAL,
                copies INTEGER
            )
        ''')
        self.connection.commit()

    def take_input(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        copies = int(input("Enter number of copies: "))

        # Check if the book already exists
        self.cursor.execute('''
            SELECT id, copies FROM books WHERE title = ? AND author = ?
        ''', (title, author))
        book = self.cursor.fetchone()

        if book:
            # If the book exists, update the number of copies
            new_copies = book[1] + copies
            self.cursor.execute('''
                UPDATE books SET copies = ?, price = ? WHERE id = ?
            ''', (new_copies, price, book[0]))
            print(f"Updated existing book. Total copies: {new_copies}")
        else:
            # If the book does not exist, insert a new record
            self.cursor.execute('''
                INSERT INTO books (title, author, price, copies)
                VALUES (?, ?, ?, ?)
            ''', (title, author, price, copies))
            print(f"Added new book: {title}")

        self.connection.commit()

    def display(self):
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        print("\nBook Details:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[3]:.2f}, Copies Available: {book[4]}")

    def sell_copies(self):
        book_id = int(input("Enter book ID to sell copies: "))
        num_copies = int(input("Enter number of copies to sell: "))
        self.cursor.execute('SELECT copies, price FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()
        if book and num_copies <= book[0]:
            total_price = num_copies * book[1]
            new_copies = book[0] - num_copies
            self.cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            self.connection.commit()
            print(f"Total Price: ${total_price:.2f}")
            print(f"Copies Remaining: {new_copies}")
        else:
            print("Insufficient copies available or book not found.")

    def refill_copies(self):
        book_id = int(input("Enter book ID to add more copies: "))
        
        self.cursor.execute('SELECT title, author, price, copies FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()

        if book:
            copies = int(input(f"Enter the number of copies to add for '{book[0]}' by {book[1]}: "))
            new_copies = book[3] + copies
            self.cursor.execute('''
                UPDATE books SET copies = ? WHERE id = ?
            ''', (new_copies, book_id))
            print(f"Updated book '{book[0]}' by {book[1]}. Total copies: {new_copies}")
        else:
            print("Book ID not found. Please try again.")

        self.connection.commit()

    def __del__(self):
        self.connection.close()

# Create an instance of the Book class
book1 = Book()

# Menu-driven program using while True and if-else
while True:
    print("\nMenu:")
    print("1. Insert New Book or Add Copies to Existing Book")
    print("2. Sell Books")
    print("3. Display Book Information")
    print("4. Refill Book Stock by ID")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        book1.take_input()
    elif choice == 2:
        book1.sell_copies()
    elif choice == 3:
        book1.display()
    elif choice == 4:
        book1.refill_copies()
    elif choice == 5:
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please try again.")
