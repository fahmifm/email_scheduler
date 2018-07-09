from app import db
from datetime import datetime
from sqlalchemy.sql import func


class Emails(db.Model):
    """
    Email model
    """

    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    email_subject = db.Column(db.String(500))
    email_content = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return 'event_id : {}'.format(self.event_id)


class Recipients(db.Model):
    """
    Recipient model
    """

    __tablename__ = 'recipients'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    email_address = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return 'email_address : {}'.format(self.email_address)
        
