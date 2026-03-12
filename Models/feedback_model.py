from Models.db import Database

def create_feedbach(self,feedback):
    db.cursor.execute(
        '''
        
        '''
    )

def get_all_feedbach(self):
    db.cursor.execute(
        '''
        SELECT * FROM feedback
        '''
    )
    feedbacks = db.cursor.fetchall()
    return feedbacks
    
