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
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f8ff')

        # Creating the GUI components with styles
        self.create_widgets()

    def create_widgets(self):
        # Book Entry Fields
        label_bg = '#add8e6'
        entry_bg = '#ffffff'
        button_bg = '#4682b4'
        button_fg = '#ffffff'
        highlight_color = '#ff6347'

        self.title_label = tk.Label(self.root, text="Title:", bg=label_bg, fg='black', font=('Arial', 12))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.title_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.author_label = tk.Label(self.root, text="Author:", bg=label_bg, fg='black', font=('Arial', 12))
        self.author_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.author_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)

        self.price_label = tk.Label(self.root, text="Price:", bg=label_bg, fg='black', font=('Arial', 12))
        self.price_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.price_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.copies_label = tk.Label(self.root, text="Copies:", bg=label_bg, fg='black', font=('Arial', 12))
        self.copies_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.copies_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.copies_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Book", bg=button_bg, fg=button_fg, activebackground=highlight_color, font=('Arial', 12), command=self.add_book)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10, ipadx=50)

        # Sell Book
        self.sell_label = tk.Label(self.root, text="Sell Book ID:", bg=label_bg, fg='black', font=('Arial', 12))
        self.sell_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.sell_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.sell_entry.grid(row=5, column=1, padx=10, pady=10)

        self.sell_copies_label = tk.Label(self.root, text="Copies to Sell:", bg=label_bg, fg='black', font=('Arial', 12))
        self.sell_copies_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.sell_copies_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.sell_copies_entry.grid(row=6, column=1, padx=10, pady=10)

        self.sell_button = tk.Button(self.root, text="Sell Book", bg=button_bg, fg=button_fg, activebackground=highlight_color, font=('Arial', 12), command=self.sell_book)
        self.sell_button.grid(row=7, column=0, columnspan=2, pady=10, ipadx=50)

        # Refill Book Stock
        self.refill_label = tk.Label(self.root, text="Refill Book ID:", bg=label_bg, fg='black', font=('Arial', 12))
        self.refill_label.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        self.refill_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.refill_entry.grid(row=8, column=1, padx=10, pady=10)

        self.refill_copies_label = tk.Label(self.root, text="Copies to Add:", bg=label_bg, fg='black', font=('Arial', 12))
        self.refill_copies_label.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        self.refill_copies_entry = tk.Entry(self.root, bg=entry_bg, fg='black', font=('Arial', 12))
        self.refill_copies_entry.grid(row=9, column=1, padx=10, pady=10)

        self.refill_button = tk.Button(self.root, text="Refill Book Stock", bg=button_bg, fg=button_fg, activebackground=highlight_color, font=('Arial', 12), command=self.refill_book)
        self.refill_button.grid(row=10, column=0, columnspan=2, pady=10, ipadx=50)

        # Display Books
        self.display_button = tk.Button(self.root, text="Display Books", bg=button_bg, fg=button_fg, activebackground=highlight_color, font=('Arial', 12), command=self.display_books)
        self.display_button.grid(row=11, column=0, columnspan=2, pady=10, ipadx=50)

        self.books_text = tk.Text(self.root, width=50, height=10, bg=entry_bg, fg='black', font=('Arial', 12))
        self.books_text.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = float(self.price_entry.get())
        copies = int(self.copies_entry.get())

        self.cursor.execute('''
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
            self.cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            self.connection.commit()
            messagebox.showinfo("Success", f"Total Price: ${total_price:.2f}\nCopies Remaining: {new_copies}")
        else:
            messagebox.showerror("Error", "Insufficient copies available or book not found.")

        self.clear_entries()

    def refill_book(self):
        book_id = int(self.refill_entry.get())
        copies = int(self.refill_copies_entry.get())

        self.cursor.execute('SELECT title, author, price, copies FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()

        if book:
            new_copies = book[3] + copies
            self.cursor.execute('''
                UPDATE books SET copies = ? WHERE id = ?
            ''', (new_copies, book_id))
            self.connection.commit()
            messagebox.showinfo("Success", f"Updated book '{book[0]}' by {book[1]}. Total copies: {new_copies}")
        else:
            messagebox.showerror("Error", "Book ID not found. Please try again.")

        self.clear_entries()

    def display_books(self):
        self.books_text.delete(1.0, tk.END)
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        for book in books:
            self.books_text.insert(tk.END, f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nPrice: {book[3]}\nCopies: {book[4]}\n\n")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
        self.sell_entry.delete(0, tk.END)
        self.sell_copies_entry.delete(0, tk.END)
        self.refill_entry.delete(0, tk.END)
        self.refill_copies_entry.delete(0, tk.END)

    def __del__(self):
        self.connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
