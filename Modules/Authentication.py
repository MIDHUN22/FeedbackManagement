import re
from Modules.db import Database
class Authentication:
    # pass
    def validate(self, name, password):

        # name should contain only letters and spaces
        if not re.fullmatch(r"[A-Za-z ]+", name):
            print("Invalid name")
            return False

        # password should not be empty
        if not password:
            print("Password cannot be empty")
            return False

    return True

    def register(self):
        print('____Register Your Self_____')
        username = input("Enter username:\t").strip()
        password = input("Enter password:\t").strip()
        role=input('Enter The Role You Want (Admin,Customer)').strip()
        
        if not self.validate(username, password):
            return
        print("Registration Successful!!!")

    def Login(self):
        print("_______Login To Account_____")
        name=input("Enter Your Name:\t").strip()
        password=input("Enter Your Password:\t").strip()
        if not self.validate(username, password):
            return

        print("Loged Successfully!!")
