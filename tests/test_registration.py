import pytest
import sqlite3
import os
from registration.registration import create_db, add_user, authenticate_user, display_users

@pytest.fixture(scope="module")
def setup_database():
    """A fixture for setting up the database before tests and cleaning up afterwards."""
    create_db()
    yield
    try:
        os.remove('users.db')
    except PermissionError:
        pass

@pytest.fixture
def connection():
    """A fixture for obtaining a database connection and closing it after a test."""
    conn = sqlite3.connect('users.db')
    yield conn
    conn.close()


def test_create_db(setup_database, connection):
    """Testing the creation of the database and the users table."""
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()
    assert table_exists, "The 'users' table should exist in the database."

def test_add_new_user(setup_database, connection):
    """Testing the addition of a new user."""
    add_user('testuser', 'testuser@example.com', 'password123')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username='testuser';")
    user = cursor.fetchone()
    assert user, "The user should be added to the database."

# Here are the tests you could write:
"""
Testing the attempt to add a user with an existing username.
Testing successful user authentication.
Testing authentication of a non-existent user.
Testing authentication with an incorrect password.
Testing the correct display of the user list.
"""