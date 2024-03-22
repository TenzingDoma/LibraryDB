import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'LibraryDB',
    'user': 'postgres',
    'password': 'Gaurav',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Define functions for database operations
def add_book():
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    availability = input("Is the book available (True/False)? ")
    genre = input("Enter genre: ")
    
    cur.execute(
        "INSERT INTO books (ISBN, TITLE, AUTHOR, AVAILABILITY, GENRE) VALUES (%s, %s, %s, %s, %s)",
        (isbn, title, author, availability, genre)
    )
    conn.commit()
    print("Book added successfully.")

def view_books():
    cur.execute("SELECT * FROM books")
    for book in cur.fetchall():
        print(book)

def update_book_availability():
    isbn = input("Enter ISBN of the book to update: ")
    availability = input("Is the book available (True/False)? ")
    
    cur.execute(
        "UPDATE books SET AVAILABILITY = %s WHERE ISBN = %s",
        (availability, isbn)
    )
    conn.commit()
    print("Book availability updated.")

def delete_book():
    isbn = input("Enter ISBN of the book to delete: ")
    
    cur.execute("DELETE FROM books WHERE ISBN = %s", (isbn,))
    conn.commit()
    print("Book deleted.")

def quit_app():
    print("Goodbye!")
    cur.close()
    conn.close()
    exit()

# User interaction loop
actions = {
    '1': add_book,
    '2': view_books,
    '3': update_book_availability,
    '4': delete_book,
    '5': quit_app
}

while True:
    print("\nChoose an action:")
    print("1 - Add a new book")
    print("2 - View all books")
    print("3 - Update a book's availability")
    print("4 - Delete a book")
    print("5 - Quit")
    
    choice = input("Enter the number of your choice: ")
    action = actions.get(choice)
    
    if action:
        action()
    else:
        print("Invalid choice, please try again.")
