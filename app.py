import os

from flask import Flask
from flask_restful import Api


from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from resources.branch import Branch, BranchList
from resources.brand import Brand, BrandList
from resources.product import Product, ProductList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'vipul'
api = Api(app)

@app.route('/')
def hello_world():
	return 'Hello world'


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Brand, '/brand/<string:name>')
api.add_resource(BrandList, '/brands')
api.add_resource(Branch, '/branch/<integer:id>')
api.add_resource(BranchList, '/branches')
api.add_resource(Product, '/product/<string:name>')
api.add_resource(ProductList, '/products')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
