import re
from Models.db import db
from Models.user_model import UserModel
from Models.customer_model import CustomerModel

class Authentication:
    # pass
    def __init__(self):
        self.user_model = UserModel()
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

    def register(self,role):
        print('____Register Your Self_____')

        username = input("Enter username:\t").strip()
        password = input("Enter password:\t").strip()

        if not self.validate(username, password):
            return

        if self.user_model.user_exist(username):
            print("User already exists")
            return

        user_id =self.user_model.create_user(username, password, role)
        if role == "Customer":

         name = username
         email = input("Enter email:\t").strip()
         phone = input("Enter phone:\t").strip()

         customer_model = CustomerModel()
         customer_model.create_customer(user_id, name, email, phone)

        print(f'Registration Successful as {role}')

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

        
