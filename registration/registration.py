import sqlite3

DB_NAME = 'users.db'

def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_user(username, email, password):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        return cursor.fetchone() is not None

def display_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, email FROM users')
        for user in cursor.fetchall():
            print(f"Logic: {user[0]}, Email: {user[1]}")


def user_choice():
    print("\n1. Login")
    print("2. Register")
    choice = input("Please enter your selection (1/2): ")
    return choice

def main():
    create_db()
    display_users()  # Show a list of users before selecting an action

    choice = user_choice()

    if choice == '1':
        username = input("Enter your login: ")
        password = input("Enter your password: ")
        if authenticate_user(username, password):
            print("Authentication complete.")
        else:
            print("Incorrect login or password.")
    elif choice == '2':
        username = input("Enter the login of the new user: ")
        email = input("Enter the email of the new user: ")
        password = input("Enter the password of the new user: ")
        add_user(username, email, password)
    else:
        print("Invalid entry. Please enter 1 to login or 2 to register.")

if __name__ == "__main__":
    main()
