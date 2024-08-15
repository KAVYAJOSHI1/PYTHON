from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    price = float(request.form['price'])
    copies = int(request.form['copies'])
    
    conn = get_db_connection()
    conn.execute('INSERT INTO books (title, author, price, copies) VALUES (?, ?, ?, ?)', 
                 (title, author, price, copies))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/display_books')
def display_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('display_books.html', books=books)

@app.route('/sell_book', methods=['POST'])
def sell_book():
    book_id = int(request.form['book_id'])
    sell_copies = int(request.form['sell_copies'])
    
    conn = get_db_connection()
    book = conn.execute('SELECT copies FROM books WHERE id = ?', (book_id,)).fetchone()
    
    if book and book['copies'] >= sell_copies:
        new_copies = book['copies'] - sell_copies
        conn.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Similar routes for refill_book, delete_book, etc.

if __name__ == '__main__':
    app.run(debug=True)
