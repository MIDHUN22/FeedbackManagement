from Models.db import db

class UserModel:

    def user_exist(self,username):
        db.cursor.execute(
            '''
            SELECT * FROM users where username=?
            ''',(username,)
        )
        return db.cursor.fetchone()

    def create_user(self, username, password, role):

        db.cursor.execute(
            '''
            INSERT INTO users(username, password, role)
            VALUES (?, ?, ?)
            ''',
            (username, password, role)
        )

        db.conn.commit()

    def login_user(self,username,password):
        db.cursor.execute(
            '''
            SELECT role FROM users WHERE username=? AND password=?
            ''',(username,password)
        )
        return db.cursor.fetchone()