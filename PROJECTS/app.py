from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        copies = request.form['copies']
        
        # Insert the new book into the database
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, price, copies) VALUES (?, ?, ?, ?)',
                       (title, author, price, copies))
        conn.commit()
        conn.close()
        
        flash('Book added successfully!')
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/display_books')
def display_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return render_template('display_books.html', books=books)

@app.route('/sell_book', methods=['GET', 'POST'])
def sell_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        sell_copies = request.form['sell_copies']
        
        # Update the book stock
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        result = cursor.fetchone()
        
        if result and result[0] >= int(sell_copies):
            new_copies = result[0] - int(sell_copies)
            cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            conn.commit()
            flash('Book sold successfully!')
        else:
            flash('Not enough copies available or invalid book ID.')
        conn.close()
        return redirect(url_for('index'))
    return render_template('sell_book.html')

@app.route('/refill_stock', methods=['GET', 'POST'])
def refill_stock():
    if request.method == 'POST':
        book_id = request.form['book_id']
        refill_copies = request.form['refill_copies']
        
        # Update the book stock
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT copies FROM books WHERE id = ?', (book_id,))
        result = cursor.fetchone()
        
        if result:
            new_copies = result[0] + int(refill_copies)
            cursor.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
            conn.commit()
            flash('Book stock refilled successfully!')
        else:
            flash('Invalid book ID.')
        conn.close()
        return redirect(url_for('index'))
    return render_template('refill_stock.html')

@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        
        # Delete the book
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()
        
        flash('Book deleted successfully!')
        return redirect(url_for('index'))
    return render_template('delete_book.html')

if __name__ == "__main__":
    app.run(debug=True)
