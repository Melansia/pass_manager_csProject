from cryptography.fernet import Fernet


class PassManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as file:
            file.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as file:
            self.key = file.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        try:
            with open(path, 'x') as file:
                file.close()
        except FileExistsError:
            print("File already exists")

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as file:
            for line in file:
                site, encrypted = line.split(':')
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                file.write(site + ':' + encrypted.decode() + '\n')

    def get_password(self, site):
        try:
            return self.password_dict[site]
        except KeyError:
            return None
