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
        if not self.validate_password(password):
            return

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

        username = input("Enter Your Name:\t").strip()
        password = input("Enter Your Password:\t").strip()

        if not self.validate(username, password):
            return None

        user = self.user_model.login_user(username, password)

        if user:
            user_id, role, status = user

            if status == "Blocked":
                print("Your account is blocked. Contact admin.")
                return None

            print("Logged In Successfully!!")
            return user_id, role

        else:
            print("Invalid Username or Password")
            return None


    def validate_password(self,password):

        if len(password) < 8:
            print("Password must be at least 8 characters")
            return False

        if not re.search("[A-Z]", password):
            print("Password must contain at least one uppercase letter")
            return False

        if not re.search("[a-z]", password):
            print("Password must contain at least one lowercase letter")
            return False

        if not re.search("[0-9]", password):
            print("Password must contain at least one number")
            return False

        if not re.search("[@#$%^&*!]", password):
            print("Password must contain at least one special character")
            return False

        return True       
