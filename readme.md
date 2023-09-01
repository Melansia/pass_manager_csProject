# Password Manager

## *Greg L*

**PassAssistant**

PassAssistant - a simple password manager, made as a final project for CS50P. It is a simple application that helps to securely store and manage passwords.
It's primary functionality is to provide a safe centralized location for storing passwords and facilitate secure retrieval of passwords when needed.
The app is running with a CLI.
Of course there is always room for improvement, maybe I will add more feature to it in the future as I will get more familiar with the coding techniques.
Like a password recovery feature Like a password recovery feature and a UI. However, for now I've device to keep it simple.

Time spend on debugging **Over 9K** hours.

## Video demontration

### << [Watch the video](https://youtu.be/AY2mS6_4t7E) >>



---
## Functionality

* Register a unique Profile and use of the Login and Password in order to get access to main menu
* Use unique Login and Password in order to encrypt and save passwords in the created Profile and then retrieve them back when needed

The following **required** functionality is completed:

* [X] When the app starts, a staring menu is prompted with the options to "Register", "Login" or "Quit" the app
* [X] Possibility to register a new Profile with a unique login and password
* [X] Possibility to login into an existing previously created profile using the Profile login and password
* [X] When registering a new Profile, each Profile is getting a unique symmetric encryption key that will be used for encrypting the passwords provided
* [X] A CLI menu for navigation

## Detailed description of the files

1. **project.py**

This file have four functions including the main functions - it is responsible for creating a database if it does not already exist which is used for storing user login information as well as displaying the main menus.
The start menu have the options to login, register, or quit the program. It prompts the user for their choice and performs the corresponding action based on the input.

In case if user try to login using incorrect login and password the user is redirected to the main manu where he can try to login again or chose to register a new profile,
in case if if the user try to register with an already existing login the user it is informed that the name already exists and is again redirected to the main menu.

Once the user login/register successful, the user is notified about the success and its redirected to the password manager menu.
It prompts the user for their choice where he can chose to add a new password - it prompts for the site/app name and password then adds it to the password manager.
If the user selects to get a password, it prompts for the site/app name and retrieves the corresponding password from the password manager. The last option is to quit the application.

Main function serves as the entry point of the application where it handles the creation of necessary directories, database, and start the application.

2. **pass_manager.py**

The Password Manager class - used OOP principle that was presented on week 8 of the CS50P course - this class provides methods to generate new unique keys for each user using the "Fernet" class from the "cryptography.fernet" module,
 as well as saving and then loading those keys individually for every user, it also help to create a password file for every user individually for a better file management where all the names of the sites/apps and encrypted passwords will be saved.

 Each password is encrypted using the stored unique key that will also be used for the decryption when the user will ty to get the password from his vault.

 The pass_manager.py file provides functionality to create and load keys, handles the password file operations and uses the unique keys created with the "Fernet" class for encryption and decryption of passwords.
 It helps with storing and retrieving the encrypted password.

3. **dir_check_create.py**

This file contains a small function that takes care of the creation of directories ( usually for every new user ) in case if thy dont already exist using the "os" module from Python to handle the file system operations.


4. **registration.py**

The file contains two functions that handle the user registration and login. It uses the SQLite database for storing user credentials, "os" module for creating a user profile directory using the function for "dir_check_create.py" mentioned above, and "bcrypt" module for hashing and salting the password before storing it to the database.

When the user register for the first time it prompts the user to enter a username and password, it connects to the users database and checks if the username already exist, if not, it hashes and lasts the password then insert the new user into the database. A user profile directory is created together with a key file and a password file specific to the user's profile.

When the user to login - it prompts the user to enter their username and password. Connects to the users database, retries the hashed passwords and checks if the password matches the stored hashed password using the "bcrypt.checkpw"
If user pass this successful, it prints a confirmation message "Login successful!", it loads the password and the key file that was created for the specific user. In case if the login fails it prints an error message.

It uses the "pass_manager.py" for managing passwords and creating unique key and password files for every user.


5. **requirements.txt**

File that contains all the pip-installable libraries for this project - listed one per line


6. **test_project.py**

File where are the testing is happening using the "pytest" framework - it coversa different scenarios and assertions to check if the program behaves correctly in different situations.

___