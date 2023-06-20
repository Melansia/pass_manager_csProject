from registration import user_registration, login_user, pm


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
            print("-" * 20)
            print("Welcome back!")
            if login_user():
                successful_login()
                running = False
        elif user_input == '2':
            print("-" * 20)
            print("Welcome to registry")
            if user_registration():
                successful_login()
                running = False
        elif user_input == 'q' or 'Q':
            running = False
            print("Bye!")


def successful_login():
    menu = """\nPassword Manager Menu:
    [1] - Create a new password file
    [2] - Load an existing password file
    [3] - Add a new password
    [4] - Get a password
    [q] - Quit
    \n"""

    running = True

    # TODO: Adding error checks
    while running:
        print(menu)
        user_input = input("Enter your choice: ")

        if user_input == '1':
            print("Feature under development")
            # pm.create_password_file(asking_for_password_path())
        elif user_input == '2':
            print("Feature under development")
            # pm.load_password_file(asking_for_password_path())
        elif user_input == '3':
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif user_input == '4':
            password_request = input("Password of what site do you search? ")
            print(f"Password for {password_request} is {pm.get_password(password_request)}")
        elif user_input == 'q' or 'Q':
            running = False
            print("Existing the app. Bye!")
        else:
            print("Invalid input!")


# def asking_for_key_path():
#     key_path = './EncKeys/'
#     return f"{key_path}{input('Enter path: ')}"


# def asking_for_password_path():
#     password_path = "./Users/"
#     return f"{password_path}{input('Enter path: ')}"


def main():
    program_start()


if __name__ == '__main__':
    main()
