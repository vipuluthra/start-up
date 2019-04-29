from db import db 
from datetime import datetime

class BranchModel(db.Model):
    __tablename__ = 'branches'

    id = db.Column(db.Integer, primary_key=True)

    brand_id = db.column(db.Integer, db.ForeignKey('brands.id'))
    brand = db.relationship('BrandModel')

    products = db.relationship('ProductModel', lazy='dynamic')

    image = db.Column() 		#

    address = db.column(db.string(80))
    phone_number = db.Column(db.Integer)
    factory_outlet = db.column(db.Boolean, unique=False, default=True)		
    has_sale = db.column(db.Boolean, unique=False, default=True)					
    salestart_date = db.column(db.DateTime, nullable=False,
        default=datetime.utcnow)			
    saleend_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)				
    created_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)				
    updated_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)				
    sale_promotion_image = db.column()			#

    def __init__(self, brand_id, image, address, phone_number, factory_outlet,has_sale,salestart_date,saleend_date, created_at, updated_at, sale_promotion_image):
    	self.brand_id = brand_id
    	self.image = image
    	self.address = address
    	self.phone_number = phone_number
    	self.factory_outlet = factory_outlet
    	self.has_sale = has_sale
    	self.salestart_date = salestart_date
    	self.saleend_date = saleend_date
    	self.created_at = created_at
        self.updated_at = updated_at
        self.sale_promotion_image = sale_promotion_image


    def json(self):
        return {'id': self.id, }                

        @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

   	def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)         
        db.session.commit()