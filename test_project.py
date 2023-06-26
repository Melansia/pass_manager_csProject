import builtins
import sqlite3
import pytest
import shutil
import os

import project
from registration import user_registration, login_user
from dir_check_create import create_directory
from project import program_start, create_db

test_prof_path = f"{os.getcwd()}\\Test_Users\\"
tes_db_path = f"{os.getcwd()}\\Test_Users\\test_db.db"


@pytest.fixture
def setup_teardown():
    # testing_path = f"{os.getcwd()}\\Test_Users"
    # Create Users directory
    create_directory(test_prof_path)
    # Create
    create_db(tes_db_path)
    # Set up any necessary resources or test data
    conn = sqlite3.connect(tes_db_path)
    cur = conn.cursor()

    # Create the users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()

    # The point where the test setup is complete, and the test function is executed
    yield
    # This part is executed after the test function finishes.

    # Clean up any files or resources were used for testing
    # Delete the test users from the user login database
    cur.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    conn.close()

    # Delete Test_Users directory with all the test users
    try:
        shutil.rmtree(test_prof_path)
    except OSError:
        print("Error when trying to delete test files")


def test_registration_unique_user(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123'])
    # Test registering a new user with a unique username
    result = user_registration(tes_db_path, test_prof_path)
    # Assert that the registration is successful
    assert result is True


def test_registration_existing_username(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123', 'SpongeBob', 'password123'])
    # Create test user
    user_registration(tes_db_path, test_prof_path)
    # Call user_registration()
    result = user_registration(tes_db_path, test_prof_path)
    # Assert that the registration fails and appropriate error message is shown
    assert result is False


def test_login_valid_credentials(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['JohnDoe', 'password123', 'JohnDoe', 'password123'])
    # Test logging in with valid credentials
    # Create test user
    user_registration(tes_db_path, test_prof_path)
    # Call login_user()
    result = login_user(tes_db_path, test_prof_path)
    # Assert that the login is successful
    assert result is True


def test_login_user_invalid_username(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123', 'Jonny', 'password123'])
    # Test logging in with an invalid username
    # Create test user
    user_registration(tes_db_path, test_prof_path)
    # Call login_user()
    result = login_user(tes_db_path, test_prof_path)
    # Assert that the login fails and appropriate error message is shown
    assert result is False


def test_login_user_invalid_password(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123', 'SpongeBob', 'password345'])
    # Test logging in with an invalid password
    # Create test user
    user_registration(tes_db_path, test_prof_path)
    # Call login_user()
    result = login_user(tes_db_path, test_prof_path)
    # Assert that the login fails and appropriate error message is shown
    assert result is False


def test_start_login(mocker):
    mocker.patch('builtins.input', side_effect=['1'])
    # Test the login flow
    mocker.patch('project.login_user', return_value=True)
    mocker.patch('project.successful_login')

    #  Starting the program
    program_start()

    # Testing the call of the login_user
    project.login_user.assert_called_once()
    # Testing the call of the successful_login
    project.successful_login.assert_called_once()


def test_start_register(mocker):
    mocker.patch('builtins.input', side_effect=['2'])
    # Test the flow of registration
    mocker.patch('project.user_registration', return_value=True)
    mocker.patch('project.successful_login')

    program_start()

    # Testing the call of the user_registration function
    project.user_registration.assert_called_once()
    # Testing the call of the successful_login unction
    project.successful_login.assert_called_once()


def test_start_quit(mocker):
    mocker.patch('builtins.input', side_effect=['q', 'Q'])
    # Test the program quitting
    mocker.patch('builtins.print')

    program_start()

    builtins.print.assert_called_with("Bye!")
