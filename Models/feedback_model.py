from Models.db import Database

class FeedbackModel:
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
    
