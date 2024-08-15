import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

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
        self.root.geometry("400x400")
        self.root.configure(bg="#e0f7fa")

        # Load images
        self.logo_image = PhotoImage(file="logo.png")  # Path to your logo image
        self.bg_image = PhotoImage(file="background.png")  # Path to your background image

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        self.style.configure('TLabel', font=('Arial', 12), background="#e0f7fa")

        # Main Menu GUI Components
        self.create_main_menu_widgets()

    def create_main_menu_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Bookstore Management System", image=self.logo_image, compound=tk.TOP)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        # Buttons stacked vertically with padding
        button_row = 1
        self.add_book_button = ttk.Button(self.root, text="Add Book", command=self.open_add_book_window)
        self.add_book_button.grid(row=button_row, column=0, padx=10, pady=10, sticky="ew")
        button_row += 1

        self.display_books_button = ttk.Button(self.root, text="Display Books", command=self.open_display_books_window)
        self.display_books_button.grid(row=button_row, column=0, padx=10, pady=10, sticky="ew")
        button_row += 1

        self.sell_book_button = ttk.Button(self.root, text="Sell Book", command=self.open_sell_book_window)
        self.sell_book_button.grid(row=button_row, column=0, padx=10, pady=10, sticky="ew")
        button_row += 1

        self.refill_stock_button = ttk.Button(self.root, text="Refill Stock", command=self.open_refill_stock_window)
        self.refill_stock_button.grid(row=button_row, column=0, padx=10, pady=10, sticky="ew")
        button_row += 1

        self.delete_book_button = ttk.Button(self.root, text="Delete Book", command=self.open_delete_book_window)
        self.delete_book_button.grid(row=button_row, column=0, padx=10, pady=10, sticky="ew")

    def open_add_book_window(self):
        AddBookWindow(self.root)

    def open_display_books_window(self):
        DisplayBooksWindow(self.root)

    def open_sell_book_window(self):
        SellBookWindow(self.root)

    def open_refill_stock_window(self):
        RefillStockWindow(self.root)

    def open_delete_book_window(self):
        DeleteBookWindow(self.root)

class AddBookWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Add Book")
        self.top.geometry("400x300")
        self.top.configure(bg="#e0f7fa")

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.configure('TLabel', font=('Arial', 12), background="#e0f7fa")
        self.style.configure('TEntry', font=('Arial', 12), padding=6)

        self.create_add_book_widgets()

    def create_add_book_widgets(self):
        # Book Entry Fields
        ttk.Label(self.top, text="Title:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.title_entry = ttk.Entry(self.top)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.top, text="Author:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.author_entry = ttk.Entry(self.top)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.top, text="Price:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = ttk.Entry(self.top)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.top, text="Copies:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.copies_entry = ttk.Entry(self.top)
        self.copies_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add Book Button
        ttk.Button(self.top, text="Add Book", command=self.add_book).grid(row=4, column=0, columnspan=2, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = float(self.price_entry.get())
        copies = int(self.copies_entry.get())

        # Database operation
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, price, copies) VALUES (?, ?, ?, ?)', 
                        (title, author, price, copies))
        conn.commit()
        conn.close()

        self.top.destroy()
        messagebox.showinfo("Success", "Book added successfully!")

class DisplayBooksWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Display Books")
        self.top.geometry("600x400")
        self.top.configure(bg="#e0f7fa")

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.configure('TLabel', font=('Arial', 12), background="#e0f7fa")

        self.create_display_books_widgets()

    def create_display_books_widgets(self):
        books_text = tk.Text(self.top, width=80, height=20, font=('Arial', 12), bg="#ffffff", wrap=tk.WORD)
        books_text.pack(padx=10, pady=10)

        # Retrieve and display books
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()

        for book in books:
            books_text.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}, Copies: {book[4]}\n")

class SellBookWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Sell Book")
        self.top.geometry("400x200")
        self.top.configure(bg="#e0f7fa")

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.configure('TLabel', font=('Arial', 12), background="#e0f7fa")
        self.style.configure('TEntry', font=('Arial', 12), padding=6)

        self.create_sell_book_widgets()

    def create_sell_book_widgets(self):
        ttk.Label(self.top, text="Book ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.book_id_entry = ttk.Entry(self.top)
        self.book_id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.top, text="Copies to Sell:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.copies_entry = ttk.Entry(self.top)
        self.copies_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(self.top, text="Sell Book", command=self.sell_book).grid(row=2, column=0, columnspan=2, pady=10)

    def sell_book(self):
        book_id = int(self.book_id_entry.get())
        sell_copies = int(self.copies_entry.get())

        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        result = cursor.fetchone()

        if result:
            if result[0] >= sell_copies:
                new_copies = result[0] - sell_copies
                cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
                conn.commit()
                conn.close()
                self.top.destroy()
                messagebox.showinfo("Success", "Book sold successfully!")
            else:
                conn.close()
                messagebox.showerror("Error", "Not enough copies available.")
        else:
            conn.close()
            messagebox.showerror("Error", "Invalid book ID.")

class RefillStockWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Refill Stock")
        self.top.geometry("400x200")
        self.top.configure(bg="#e0f7fa")

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.configure('TLabel', font=('Arial', 12), background="#e0f7fa")
        self.style.configure('TEntry', font=('Arial', 12), padding=6)

        self.create_refill_stock_widgets()

    def create_refill_stock_widgets(self):
        ttk.Label(self.top, text="Book ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.book_id_entry = ttk.Entry(self.top)
        self.book_id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.top, text="Copies to Add:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.copies_entry = ttk.Entry(self.top)
        self.copies_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(self.top, text="Refill Stock", command=self.refill_stock).grid(row=2, column=0, columnspan=2, pady=10)

    def refill_stock(self):
        book_id = int(self.book_id_entry.get())
        refill_copies = int(self.copies_entry.get())

        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        result = cursor.fetchone()

        if result:
            new_copies = result[0] + refill_copies
            cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            conn.commit()
            conn.close()
            self.top.destroy()
            messagebox.showinfo("Success", "Stock refilled successfully!")
        else:
            conn.close()
            messagebox.showerror("Error", "Invalid book ID.")

class DeleteBookWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Delete Book")
        self.top.geometry("400x200")
        self.top.configure(bg="#e0f7fa")

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.configure('TLabel', font=('Arial', 12), background="#e0f7fa")
        self.style.configure('TEntry', font=('Arial', 12), padding=6)

        self.create_delete_book_widgets()

    def create_delete_book_widgets(self):
        ttk.Label(self.top, text="Book ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.book_id_entry = ttk.Entry(self.top)
        self.book_id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(self.top, text="Delete Book", command=self.delete_book).grid(row=1, column=0, columnspan=2, pady=10)

    def delete_book(self):
        book_id = int(self.book_id_entry.get())

        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()

        if cursor.rowcount > 0:
            conn.close()
            self.top.destroy()
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            conn.close()
            messagebox.showerror("Error", "Book ID not found.")

# Create the main window
root = tk.Tk()
app = BookApp(root)
root.mainloop()
