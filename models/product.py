from db import db

class ProductModel (db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.column(db.Integer, db.ForeignKey('branches.id'))
    branch = db.relationship('BranchModel')

    starting_from = db.column(db.Integer)		#price starting from 
    name = db.column(db.string)                 
    sale_percentage = db.column(db.Integer)
    product_image = db.Column() 			#

    def __init__(self, branch_id, starting_from, name, sale_percentage, product_image):
    	self.branch_id = branch_id
    	self.starting_from = starting_from
    	self.name = name
        self.sale_percentage = sale_percentage
        self.product_image = product_image

    def json(self):
        return {'name': self.name, }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()