import sqlite3
import os

from registration import user_registration, login_user, pm
from dir_check_create import create_directory


def create_db(path=f"{os.getcwd()}/Users/users.db"):
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
        elif user_input == 'q' or user_input == 'Q':
            running = False
            print("Bye!")
        else:
            print("Non existing command! Try 1, 2 or q|Q for quiting.")


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
            print(f"\nPassword for {site} was saved successfully! You can find it in your vault.")
        elif user_input == '2':
            password_request = input("Password of what site do you search? ")
            get_pass = pm.get_password(password_request)
            print(f"\nPassword for {password_request} is {get_pass if get_pass is not None else 'not yet created.'}")
        elif user_input == 'q' or user_input == 'Q':
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
