import builtins
import sqlite3
import pytest

import project
from registration import user_registration, login_user
from dir_check_create import create_directory
from project import program_start, create_db


@pytest.fixture
def setup_teardown():
    # Create Users directory
    create_directory()
    # Create
    create_db()
    # Set up any necessary resources or test data
    conn = sqlite3.connect("./Users/user_login.db")
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

    yield

    # Clean up any resources used for testing
    # Delete the test user from the user login database
    cur.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    conn.close()


def test_user_registration_unique_username(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123'])
    # Test registering a new user with a unique username
    result = user_registration()
    # Assert that the registration is successful
    assert result is True


def test_user_registration_existing_username(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123', 'SpongeBob', 'password123'])
    # Create test user
    user_registration()
    # Call user_registration()
    result = user_registration()
    # Assert that the registration fails and appropriate error message is shown
    assert result is False


def test_login_user_valid_credentials(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['JohnDoe', 'password123', 'JohnDoe', 'password123'])
    # Test logging in with valid credentials
    # Create test user
    user_registration()
    # Call login_user()
    result = login_user()
    # Assert that the login is successful
    assert result is True


def test_login_user_invalid_username(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123', 'Jonny', 'password123'])
    # Test logging in with an invalid username
    # Create test user
    user_registration()
    # Call login_user()
    result = login_user()
    # Assert that the login fails and appropriate error message is shown
    assert result is False


def test_login_user_invalid_password(setup_teardown, mocker):
    mocker.patch('builtins.input', side_effect=['SpongeBob', 'password123', 'SpongeBob', 'password345'])
    # Test logging in with an invalid password
    # Create test user
    user_registration()
    # Call login_user()
    result = login_user()
    # Assert that the login fails and appropriate error message is shown
    assert result is False


def test_program_start_login(mocker):
    mocker.patch('builtins.input', side_effect=['1'])
    # Test the login flow
    mocker.patch('project.login_user', return_value=True)
    mocker.patch('project.successful_login')

    #  Starting the program
    program_start()

    # Testing that the login user was called
    project.login_user.assert_called_once()
    # Testing that the successful_login was called
    project.successful_login.assert_called_once()


def test_program_start_register(mocker):
    mocker.patch('builtins.input', side_effect=['2'])
    # Test the registration flow
    mocker.patch('project.user_registration', return_value=True)
    mocker.patch('project.successful_login')

    program_start()

    project.user_registration.assert_called_once()
    project.successful_login.assert_called_once()



def test_program_start_quit(mocker):
    mocker.patch('builtins.input', side_effect=['q', 'Q'])
    # Test quitting the program
    mocker.patch('builtins.print')

    program_start()

    builtins.print.assert_called_with("Bye!")
