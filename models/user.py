from db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.column(db.string(80))
    lastname = db.column(db.string(80))
    current_location = db.column(db.string(80))
    phone_number = db.Column(db.Integer)
    e_mail = db.Column(db.string(80) unique=True, nullable=False)				
    username = db.Column(db.String(80) unique=True, nullable=False)
    password = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)				
    updated_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)				

    def __init__(self, firstname, lastname, current_location, phone_number, email, username, password, created_at, updated_at):
    	self.firstname = firstname
    	self.lastname = lastname
    	self.current_location = current_location
    	self.phone_number = phone_number
    	self.email = email
	self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
