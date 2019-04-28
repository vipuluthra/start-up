from db import db

class BrandModel(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(80))
    description = db.column(db.string(80))
    created_at = db.Column(db.Date)				#
    updated_at = db.Column(db.Date)				#

    branches = db.relationship('BranchModel', lazy='dynamic')


    def __init__(self, name, description, created_at, updated_at):
    	self.firstname = name
    	self.lastname = description
    	self.created_at = created_at
        self.updated_at = updated_at

 	def json(self):
        return {'name': self.name, }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

   	def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()