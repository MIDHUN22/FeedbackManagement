from Models.db import db
class CustomerModel:
    def create_customer(self, user_id, name, email, phone):

        db.cursor.execute(
            '''
            INSERT INTO customers (user_id, name, email, phone)
            VALUES (?, ?, ?, ?)
            ''',
            (user_id, name, email, phone)
        )

        db.conn.commit()
    
    def get_customer_by_user_id(self, user_id):
        db.cursor.execute(
            '''
            SELECT customer_id FROM customers WHERE user_id=?
            ''',
            (user_id,)
        )
        return db.cursor.fetchone()
    