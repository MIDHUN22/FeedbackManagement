import re
from Models.db import db
from Models.user_model import UserModel

class Authentication:
    # pass
    def validate(self, username, password):

        # name should contain only letters and spaces
        if not re.fullmatch(r"[A-Za-z ]+", username):
            print("Invalid username")
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
        role = input("Enter The Role You Want (Admin,Customer): ").strip()

        if not self.validate(username, password):
            return

        if self.user_model.user_exist(username):
            print("User already exists")
            return

        self.user_model.create_user(username, password, role)

        print("Registration Successful!!!")

    def Login(self):
        print("_______Login To Account_____")
        username=input("Enter Your Name:\t").strip()
        password=input("Enter Your Password:\t").strip()
        if not self.validate(username, password):
            return
        role=self.user_model.login_user(username,password)
        if role:
            print("Loged In Successfully!!")
            return role[0]
        else:
            print('Role Not Found,Invalid Username or password')

        
