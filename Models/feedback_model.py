from Models.db import db

class FeedbackModel:

    def create_feedback(self, customer_id, product_id, rating, comment):

        db.cursor.execute(
            '''
            INSERT INTO feedback (customer_id, product_id, rating, comment)
            VALUES (?, ?, ?, ?)
            ''',
            (customer_id, product_id, rating, comment)
        )

        db.conn.commit()


    def get_all_feedback(self):

        db.cursor.execute(
            '''
            SELECT * FROM feedback
            '''
        )

        return db.cursor.fetchall()


    def get_all_customer_feedback(self, customer_id):

        db.cursor.execute(
        '''
        SELECT users.username,
               products.product_name,
               feedback.comment,
               feedback.rating,
               feedback.status
        FROM feedback
        JOIN customers ON feedback.customer_id = customers.customer_id
        JOIN users ON customers.user_id = users.user_id
        JOIN products ON feedback.product_id = products.product_id
        WHERE feedback.customer_id = ?
        ''',
        (customer_id,)
    )

        return db.cursor.fetchall()


    def change_status(self, feedback_id, status):

        db.cursor.execute(
            '''
            UPDATE feedback
            SET status = ?
            WHERE feedback_id = ?
            ''',
            (status, feedback_id)
        )

        db.conn.commit()

        print("Feedback status updated successfully")