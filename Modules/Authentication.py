import re
from Models.db import db
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
        role=input('Enter The Role You Want (Admin,Customer)').strip()
        
        if not self.validate(username, password):
            return

        db.cursor.execute(
            "SELECT 1 FROM users WHERE username=?",
            (username,)
        )
        
        if db.cursor.fetchone():
            print("User already exists")
            return

        db.cursor.execute(
            '''
            INSERT INTO users(username,password,role)
            VALUES(?,?,?)
            ''',
            (username, password, role)
        )
        if db.conn.commit():
            print("Registration Successful!!!")
        else:
            print('Somethong Went Wrong')
            return

    def Login(self):
        print("_______Login To Account_____")
        username=input("Enter Your Name:\t").strip()
        password=input("Enter Your Password:\t").strip()
        if not self.validate(username, password):
            return

        print("Loged Successfully!!")
