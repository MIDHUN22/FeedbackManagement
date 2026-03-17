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

    def get_customers(self):
        db.cursor.execute(
        '''
        SELECT customers.customer_id,
               users.username,
               customers.name,
               customers.email,
               customers.phone
        FROM customers
        JOIN users
        ON customers.user_id = users.user_id
        '''
        )
        return db.cursor.fetchall()
        
    def delete_customer(self, customer_id):

        db.cursor.execute(
            '''
            SELECT user_id FROM customers WHERE customer_id=?
            ''',
            (customer_id,)
        )

        user_id = db.cursor.fetchone()[0]

        db.cursor.execute(
            '''
            DELETE FROM customers WHERE customer_id=?
            ''',
            (customer_id,)
        )

        db.cursor.execute(
            '''
            DELETE FROM users WHERE user_id=?
            ''',
            (user_id,)
        )

        db.conn.commit()
    