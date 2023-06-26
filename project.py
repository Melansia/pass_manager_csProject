import sqlite3
import os

from registration import user_registration, login_user, pm
from dir_check_create import create_directory


def create_db(path=f"{os.getcwd()}\\Users\\users.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    )""")

    cur.close()


def program_start():
    start_menu = """\nWelcome to Password Manager:
    [1] - Login
    [2] - Register
    [q] - Quit
    \n"""

    running = True

    while running:
        print(start_menu)
        user_input = input("Enter your choice: ")

        if user_input == '1':
            print()
            print("Welcome back!")
            if login_user():
                successful_login()
                running = False
        elif user_input == '2':
            print()
            print("Welcome to registry")
            if user_registration():
                successful_login()
                running = False
        elif user_input == 'q' or 'Q':
            running = False
            print("Bye!")


def successful_login():
    menu = """\nPassword Manager Menu:
    [1] - Add a new password
    [2] - Get a password
    [q] - Quit
    \n"""

    running = True

    while running:
        print(menu)
        user_input = input("Enter your choice: ")

        if user_input == '1':
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif user_input == '2':
            password_request = input("Password of what site do you search? ")
            print(f"Password for {password_request} is {pm.get_password(password_request)}")
        elif user_input == 'q' or 'Q':
            running = False
            print("Existing the app. Bye!")
        else:
            print("Invalid input!")


def main():
    # Create Users directory in case if is not created at default location
    create_directory()
    # Create users database at the default location
    create_db()

    program_start()


if __name__ == '__main__':
    main()
