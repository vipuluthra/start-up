from flask_restful import Resource, reqparse

from models.product import ProductModel


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('branch_id',
                        type=int,
                        required=True,
                        help="Every product needs a branch_id."
                        )

    
    def get(self, name):                            
        product = ProductModel.find_by_name(name)
        if product:
            return product.json()
        return {'message': 'Product not found'}, 404

    def post(self, name):
        if ProductModel.find_by_name(name):
            return {'message': "A product with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        product = ProductModel(name, **data)

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the product."}, 500

        return product.json(), 201

    def delete(self, name):
        product = ProductModel.find_by_name(name)
        if product:
            product.delete_from_db()

        return {'message': 'Product deleted'}


class ProductList(Resource):                
    def get(self):
        return {'products': list(map(lambda x: x.json(), ProductModel.query.all()))}