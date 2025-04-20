# A User Management System

A simple user management system implemented in Python. This system uses SQLite for user data storage. The program allows adding new users, authenticating existing users, and displaying a list of all registered users.

## Features

- **Adding new users**: The app saves the login data of the new users in the database
- **User authentication**: The app verifies user credentials before authentication.
- **Display user list**: The app outputs a list of all users with their data (excluding passwords).

## Getting Started

To use this program, ensure you have Python version 3.6 or higher and SQLite installed.

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone repository_path
    ```
2. Navigate to the project directory:
    ```bash
    cd User_Management_System_DB
    ```

### Usage

To run the program, execute the following command in your terminal:
```bash
python registration.py
```
Follow the on-screen instructions to manage users.

### Testing

The program includes unit tests written using the pytest library. To run the tests, ensure pytest is installed (install via pip if needed):
```bash
pip install pytest
```

Run tests from the project's root directory with the following command:
```bash
pytest
```
## Author

Kodland