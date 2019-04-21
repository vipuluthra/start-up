
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.column(db.string(80))
    lastname = db.column(db.string(80))
    current_location = db.column(db.string(80))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.string(80))				#
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    created_at = db.Column(db.Integer)				#
    updated_at = db.Column(db.Integer)				#

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


class Brand(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.string(80))
    description = db.column(db.string(80))
    created_at = db.Column(db.Date)				#
    updated_at = db.Column(db.Date)				#

    def __init__(self, name, description, created_at, updated_at):
    	self.firstname = name
    	self.lastname = description
    	self.created_at = created_at
        self.updated_at = updated_at


class Branch(db.Model):
    __tablename__ = 'branch'

    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.column(db.Integer)
    image = db.Column() 									#
    address = db.column(db.string(80))
    phone_number = db.Column(db.Integer)
    factory_outlet = db.column()			#
    has_sale = db.column()					#
    salestart_date = db.column()			#
    saleend_date = db.Column()				#
    created_at = db.Column(db.Date)				#
    updated_at = db.Column(db.Date)				#
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

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.column(db.Integer)
    starting_from = db.column(db.Integer)		#
    name = db.column(db.string)
    sale_percentage = db.column(db.Integer)
    product_image = db.Column() 			#

    def __init__(self, branch_id, starting_from, name, sale_percentage, product_image):
    	self.branch_id = branch_id
    	self.starting_from = starting_from
    	self.name = name
        self.sale_percentage = sale_percentage
        self.product_image = product_image

class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.column(db.Integer)
    branch_id = db.column(db.Integer)	
    user_id = db.column()						# 								
    created_at = db.Column(db.Date)				#
    updated_at = db.Column(db.Date)				#

    def __init__(self, rating, branch_id, user_id, created_at, updated_at):
    	self.rating = rating
    	self.branch_id = branch_id
    	self.user_id = user_id
    	self.created_at = created_at
        self.updated_at = updated_at


