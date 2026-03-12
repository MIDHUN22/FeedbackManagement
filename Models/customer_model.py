from Models.db import Database
class CustomerModel:
     def create_customer(self, user_id, name, email, phone):

        db.cursor.execute(
            '''
            INSERT INTO customer (user_id, name, email, phone)
            VALUES (?, ?, ?, ?)
            ''',
            (user_id, name, email, phone)
        )

        db.conn.commit()