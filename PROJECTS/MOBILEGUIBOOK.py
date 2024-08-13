import sqlite3
import tkinter as tk
from tkinter import messagebox

class BookApp:
    def __init__(self, root):
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

        self.root = root
        self.root.title("Bookstore Management")

        # Creating the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Book Entry Fields
        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.author_label = tk.Label(self.root, text="Author:")
        self.author_label.grid(row=1, column=0, padx=10, pady=10)
        self.author_entry = tk.Entry(self.root)
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)

        self.price_label = tk.Label(self.root, text="Price:")
        self.price_label.grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.copies_label = tk.Label(self.root, text="Copies:")
        self.copies_label.grid(row=3, column=0, padx=10, pady=10)
        self.copies_entry = tk.Entry(self.root)
        self.copies_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Sell Book
        self.sell_label = tk.Label(self.root, text="Sell Book ID:")
        self.sell_label.grid(row=5, column=0, padx=10, pady=10)
        self.sell_entry = tk.Entry(self.root)
        self.sell_entry.grid(row=5, column=1, padx=10, pady=10)

        self.sell_copies_label = tk.Label(self.root, text="Copies to Sell:")
        self.sell_copies_label.grid(row=6, column=0, padx=10, pady=10)
        self.sell_copies_entry = tk.Entry(self.root)
        self.sell_copies_entry.grid(row=6, column=1, padx=10, pady=10)

        self.sell_button = tk.Button(self.root, text="Sell Book", command=self.sell_book)
        self.sell_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Refill Book Stock
        self.refill_label = tk.Label(self.root, text="Refill Book ID:")
        self.refill_label.grid(row=8, column=0, padx=10, pady=10)
        self.refill_entry = tk.Entry(self.root)
        self.refill_entry.grid(row=8, column=1, padx=10, pady=10)

        self.refill_copies_label = tk.Label(self.root, text="Copies to Add:")
        self.refill_copies_label.grid(row=9, column=0, padx=10, pady=10)
        self.refill_copies_entry = tk.Entry(self.root)
        self.refill_copies_entry.grid(row=9, column=1, padx=10, pady=10)

        self.refill_button = tk.Button(self.root, text="Refill Book Stock", command=self.refill_book)
        self.refill_button.grid(row=10, column=0, columnspan=2, pady=10)

        # Display Books
        self.display_button = tk.Button(self.root, text="Display Books", command=self.display_books)
        self.display_button.grid(row=11, column=0, columnspan=2, pady=10)

        self.books_text = tk.Text(self.root, width=50, height=10)
        self.books_text.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = float(self.price_entry.get())
        copies = int(self.copies_entry.get())

        # Check if the book already exists
        self.cursor.execute('''
            SELECT id, copies FROM books WHERE title = ? AND author = ?
        ''', (title, author))
        book = self.cursor.execute('''
            SELECT id, copies FROM books WHERE title = ? AND author = ?
        ''', (title, author))
        book = self.cursor.fetchone()

        if book:
            new_copies = book[1] + copies
            self.cursor.execute('''
                UPDATE books SET copies = ?, price = ? WHERE id = ?
            ''', (new_copies, price, book[0]))
            messagebox.showinfo("Success", f"Updated existing book. Total copies: {new_copies}")
        else:
            self.cursor.execute('''
                INSERT INTO books (title, author, price, copies)
                VALUES (?, ?, ?, ?)
            ''', (title, author, price, copies))
            messagebox.showinfo("Success", f"Added new book: {title}")

        self.connection.commit()
        self.clear_entries()

    def sell_book(self):
        book_id = int(self.sell_entry.get())
        num_copies = int(self.sell_copies_entry.get())
        self.cursor.execute('SELECT copies, price FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()
        if book and num_copies <= book[0]:
            total_price = num_copies * book[1]
            new_copies = book[0] - num_copies
            self.cursor.execute('''
                UPDATE books SET copies = ? WHERE id = ?
            ''', (new_copies, book_id))
            messagebox.showinfo("Success", f"Sold {num_copies} copies of book {book_id}. Total price: ${total_price:.2f}")
        else:
            messagebox.showerror("Error", "Not enough copies in stock")
        self.connection.commit()
        self.clear_entries()

    def refill_book(self):
        book_id = int(self.refill_entry.get())
        num_copies = int(self.refill_copies_entry.get())
        self.cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()
        if book:
            new_copies = book[0] + num_copies
            self.cursor.execute('''
                UPDATE books SET copies = ? WHERE id = ?
            ''', (new_copies, book_id))
            messagebox.showinfo("Success", f"Refilled book {book_id} with {num_copies} copies. Total copies: {new_copies}")
        else:
            messagebox.showerror("Error", "Book not found")
        self.connection.commit()
        self.clear_entries()

    def display_books(self):
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        self.books_text.delete(1.0, tk.END)
        for book in books:
            self.books_text.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[3]:.2f}, Copies: {book[4]}\n")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
        self.sell_entry.delete(0, tk.END)
        self.sell_copies_entry.delete(0, tk.END)
        self.refill_entry.delete(0, tk.END)
        self.refill_copies_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()