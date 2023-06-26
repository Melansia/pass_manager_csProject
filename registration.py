import sqlite3
import os
import bcrypt
from pass_manager import PassManager
from dir_check_create import create_directory

pm = PassManager()


def user_registration(db_path=f"{os.getcwd()}\\Users\\users.db", prof_path=f"{os.getcwd()}\\Users\\"):
    # Users database path

    # Getting user username and password
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Connect to the user login database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Check if the username already exists
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cur.fetchone()

    if existing_user:
        print("Username already exists. Please choose a different username.")
        conn.close()
        return False

    # Hash and salt the password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Insert the new user into the database
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

    print(f"Hey, {username}, the registration was successful!")
    conn.close()

    profile_path = f"{prof_path}{username}"
    create_directory(profile_path)
    pm.create_key(f"{profile_path}/{username}.key")
    pm.create_password_file(f"{profile_path}/{username}.json")

    return True


def login_user(db_path=f"{os.getcwd()}\\Users\\users.db", prof_path=f"{os.getcwd()}\\Users\\"):
    # Users path
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Connect to the user login database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Retrieve the stored hashed password for the entered username
    # TODO: Check if the table is created
    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cur.fetchone()

    if not stored_password:
        print("Invalid username. Please try again.")
        conn.close()
        return False

    # Check if the entered password matches the stored hashed password
    if bcrypt.checkpw(password.encode(), stored_password[0]):
        print("Login successful!")
        # Get path of the profile that was successful login
        profile_path = prof_path
        pass_file_path = f"{profile_path}{username}\\{username}.json"
        # Load the key and the password file for the profile
        pm.load_key(f"{profile_path}{username}\\{username}.key")
        pm.load_password_file(pass_file_path)
        return True
    else:
        print("Invalid password. Please try again.")
        conn.close()
        return False
