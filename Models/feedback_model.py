from Models.db import Database

class FeedbackModel:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor
        
    def create_feedback(self,feedback):
     db.cursor.execute(
        '''
        
        '''
    )

    def get_all_feedback(self):
        db.cursor.execute(
        '''
        SELECT * FROM feedback
        '''
    )
        feedbacks = db.cursor.fetchall()
        return feedbacks
    
    def get_all_customer_feedback(self,role):
        db.cursor.execute(
            '''
            Select * from feedback where role='Customer'
            '''
        )
        feedbacks = db.cursor.fetchall()
        return feedbacks

