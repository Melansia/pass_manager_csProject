from pass_manager import PassManager


def main():
    # Code for test purposes
    passwords = {
        "Google": "1234567",
        "Youtube": "veryStronkPassword",
        "iBank": "pleaseDontTakeMyMoney",
        "Steam": "AnotherStronkPassword_12",
        "email": 'veyverystronk'
    }

    pm = PassManager()

    menu = """Password Manager Menu:
    [1] - Create a new key
    [2] - Load an existing key
    [3] - Create a new password file
    [4] - Load an existing password file
    [5] - Add a new password
    [6] - Get a password
    [q] - Quit
    """

    running = True

    while running:
        print(menu)
        user_input = input("Enter your choice: ")

        if user_input == '1':
            pm.create_key(asking_for_key_path())
        elif user_input == '2':
            pm.load_key(asking_for_key_path())
        elif user_input == '3':
            pm.create_password_file(asking_for_password_path(), passwords)
        elif user_input == '4':
            pm.load_password_file(asking_for_password_path())
        elif user_input == '5':
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif user_input == '6':
            password_request = input("Password of what site do you search? ")
            print(f"Password for {password_request} is {pm.get_password(password_request)}")
        elif user_input == 'q' or 'Q':
            running = False
            print("Existing the app. Bye!")
        else:
            print("Invalid input!")


def asking_for_key_path():
    key_path = './EncKeys/'
    return f"{key_path}{input('Enter path: ')}"


def asking_for_password_path():
    password_path = "./Store/"
    return f"{password_path}{input('Enter path: ')}"


if __name__ == '__main__':
    main()
