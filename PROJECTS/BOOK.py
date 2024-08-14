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
        self.root.configure(bg="#f0f0f0")

        # Creating the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Book Entry Fields
        self.title_label = tk.Label(self.root, text="Title:", font=('Arial', 12), bg="#f0f0f0")
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.title_entry = tk.Entry(self.root, font=('Arial', 12))
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        self.author_label = tk.Label(self.root, text="Author:", font=('Arial', 12), bg="#f0f0f0")
        self.author_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.author_entry = tk.Entry(self.root, font=('Arial', 12))
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        self.price_label = tk.Label(self.root, text="Price:", font=('Arial', 12), bg="#f0f0f0")
        self.price_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = tk.Entry(self.root, font=('Arial', 12))
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        self.copies_label = tk.Label(self.root, text="Copies:", font=('Arial', 12), bg="#f0f0f0")
        self.copies_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.copies_entry = tk.Entry(self.root, font=('Arial', 12))
        self.copies_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add Book Button
        self.add_button = tk.Button(self.root, text="Add Book", font=('Arial', 12), bg="#4CAF50", fg="white", command=self.add_book)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.add_button.bind("<Enter>", lambda e: e.widget.configure(bg="#45a049"))
        self.add_button.bind("<Leave>", lambda e: e.widget.configure(bg="#4CAF50"))

        # Sell Book Section
        self.sell_label = tk.Label(self.root, text="Sell Book ID:", font=('Arial', 12), bg="#f0f0f0")
        self.sell_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.sell_entry = tk.Entry(self.root, font=('Arial', 12))
        self.sell_entry.grid(row=5, column=1, padx=10, pady=5)

        self.sell_copies_label = tk.Label(self.root, text="Copies to Sell:", font=('Arial', 12), bg="#f0f0f0")
        self.sell_copies_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.sell_copies_entry = tk.Entry(self.root, font=('Arial', 12))
        self.sell_copies_entry.grid(row=6, column=1, padx=10, pady=5)

        self.sell_button = tk.Button(self.root, text="Sell Book", font=('Arial', 12), bg="#2196F3", fg="white", command=self.sell_book)
        self.sell_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.sell_button.bind("<Enter>", lambda e: e.widget.configure(bg="#1e88e5"))
        self.sell_button.bind("<Leave>", lambda e: e.widget.configure(bg="#2196F3"))

        # Refill Book Stock Section
        self.refill_label = tk.Label(self.root, text="Refill Book ID:", font=('Arial', 12), bg="#f0f0f0")
        self.refill_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.refill_entry = tk.Entry(self.root, font=('Arial', 12))
        self.refill_entry.grid(row=8, column=1, padx=10, pady=5)

        self.refill_copies_label = tk.Label(self.root, text="Copies to Add:", font=('Arial', 12), bg="#f0f0f0")
        self.refill_copies_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.refill_copies_entry = tk.Entry(self.root, font=('Arial', 12))
        self.refill_copies_entry.grid(row=9, column=1, padx=10, pady=5)

        self.refill_button = tk.Button(self.root, text="Refill Book Stock", font=('Arial', 12), bg="#FFC107", fg="white", command=self.refill_book)
        self.refill_button.grid(row=10, column=0, columnspan=2, pady=10)
        self.refill_button.bind("<Enter>", lambda e: e.widget.configure(bg="#ffb300"))
        self.refill_button.bind("<Leave>", lambda e: e.widget.configure(bg="#FFC107"))

        # Delete Book Section
        self.delete_label = tk.Label(self.root, text="Delete Book ID:", font=('Arial', 12), bg="#f0f0f0")
        self.delete_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.delete_entry = tk.Entry(self.root, font=('Arial', 12))
        self.delete_entry.grid(row=11, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Book", font=('Arial', 12), bg="#f44336", fg="white", command=self.delete_book)
        self.delete_button.grid(row=12, column=0, columnspan=2, pady=10)
        self.delete_button.bind("<Enter>", lambda e: e.widget.configure(bg="#e53935"))
        self.delete_button.bind("<Leave>", lambda e: e.widget.configure(bg="#f44336"))

        # Display Books Button
        self.display_button = tk.Button(self.root, text="Display Books", font=('Arial', 12), bg="#9C27B0", fg="white", command=self.display_books)
        self.display_button.grid(row=13, column=0, columnspan=2, pady=10)
        self.display_button.bind("<Enter>", lambda e: e.widget.configure(bg="#8e24aa"))
        self.display_button.bind("<Leave>", lambda e: e.widget.configure(bg="#9C27B0"))

        self.books_text = tk.Text(self.root, width=60, height=10, font=('Arial', 12))
        self.books_text.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = float(self.price_entry.get())
        copies = int(self.copies_entry.get())
        
        self.cursor.execute('INSERT INTO books (title, author, price, copies) VALUES (?, ?, ?, ?)', 
                            (title, author, price, copies))
        self.connection.commit()
        
        self.clear_entries()
        messagebox.showinfo("Success", "Book added successfully!")

    def sell_book(self):
        book_id = int(self.sell_entry.get())
        sell_copies = int(self.sell_copies_entry.get())
        
        self.cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        result = self.cursor.fetchone()
        
        if result and result[0] >= sell_copies:
            new_copies = result[0] - sell_copies
            self.cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            self.connection.commit()
            messagebox.showinfo("Success", "Book sold successfully!")
        else:
            messagebox.showerror("Error", "Not enough copies available or invalid book ID.")
        
        self.clear_entries()

    def refill_book(self):
        book_id = int(self.refill_entry.get())
        refill_copies = int(self.refill_copies_entry.get())
        
        self.cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        result = self.cursor.fetchone()
        
        if result:
            new_copies = result[0] + refill_copies
            self.cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            self.connection.commit()
            messagebox.showinfo("Success", "Book stock refilled successfully!")
        else:
            messagebox.showerror("Error", "Invalid book ID.")
        
        self.clear_entries()

    def delete_book(self):
        book_id = int(self.delete_entry.get())
        
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.connection.commit()
        
        if self.cursor.rowcount > 0:
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showerror("Error", "Invalid book ID.")
        
        self.clear_entries()

    def display_books(self):
        self.books_text.delete(1.0, tk.END)
        
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        
        for book in books:
            self.books_text.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}, Copies: {book[4]}\n")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
        self.sell_entry.delete(0, tk.END)
        self.sell_copies_entry.delete(0, tk.END)
        self.refill_entry.delete(0, tk.END)
        self.refill_copies_entry.delete(0, tk.END)
        self.delete_entry.delete(0, tk.END)

    def __del__(self):
        self.connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
