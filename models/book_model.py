from db import conn, cursor

def get_all_books():
    cursor.execute("SELECT * FROM books;")
    return cursor.fetchall()

def get_book(book_id):
    cursor.execute("SELECT * FROM books WHERE id = %s;", (book_id,))
    return cursor.fetchone()

def create_book(data):
    cursor.execute(
        "INSERT INTO books (title, author, price, quantity) VALUES (%s, %s, %s, %s) RETURNING *;",
        (data["title"], data["author"], data["price"], data["quantity"])
    )
    conn.commit()
    return cursor.fetchone()

def update_book(book_id, data):
    cursor.execute(
        "UPDATE books SET title=%s, author=%s, price=%s, quantity=%s WHERE id=%s RETURNING *;",
        (data["title"], data["author"], data["price"], data["quantity"], book_id)
    )
    conn.commit()
    return cursor.fetchone()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = %s;", (book_id,))
    conn.commit()
