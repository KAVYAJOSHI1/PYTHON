from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for session management

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

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

        conn = get_db_connection()
        conn.execute('INSERT INTO books (title, author, price, copies) VALUES (?, ?, ?, ?)',
                     (title, author, price, copies))
        conn.commit()
        conn.close()

        flash('Book added successfully!')
        return redirect(url_for('index'))

    return render_template('add_book.html')

@app.route('/display_books')
def display_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('display_books.html', books=books)

@app.route('/sell_book', methods=['GET', 'POST'])
def sell_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        sell_copies = int(request.form['sell_copies'])

        conn = get_db_connection()
        book = conn.execute('SELECT copies FROM books WHERE id = ?', (book_id,)).fetchone()

        if book:
            new_copies = book['copies'] - sell_copies
            if new_copies < 0:
                flash('Not enough copies to sell!')
            else:
                conn.execute('UPDATE books SET copies = ? WHERE id = ?', (new_copies, book_id))
                conn.commit()
                flash('Book sold successfully!')
        else:
            flash('Book not found!')

        conn.close()
        return redirect(url_for('index'))

    return render_template('sell_book.html')

@app.route('/refill_stock', methods=['GET', 'POST'])
def refill_stock():
    if request.method == 'POST':
        book_id = request.form['book_id']
        refill_copies = int(request.form['refill_copies'])

        conn = get_db_connection()
        conn.execute('UPDATE books SET copies = copies + ? WHERE id = ?', (refill_copies, book_id))
        conn.commit()
        conn.close()

        flash('Stock refilled successfully!')
        return redirect(url_for('index'))

    return render_template('refill_stock.html')

@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'POST':
        book_id = request.form['book_id']

        conn = get_db_connection()
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()

        flash('Book deleted successfully!')
        return redirect(url_for('index'))

    return render_template('delete_book.html')

if __name__ == '__main__':
    app.run(debug=True)
