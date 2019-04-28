from flask_restful import Resource
from models.brand import BrandModel


class Brand(Resource):
    def get(self, name):
        brand = BrandModel.find_by_name(name)
        if brand:
            return brand.json()
        return {'message': 'Brand not found'}, 404

    def post(self, name):
        if BrandModel.find_by_name(name):
            return {'message': "A brand with name '{}' already exists.".format(name)}, 400

        brand = BrandModel(name)
        try:
            brand.save_to_db()
        except:
            return {"message": "An error occurred creating the brand."}, 500

        return brand.json(), 201

    def delete(self, name):
        brand = BrandModel.find_by_name(name)
        if brand:
            brand.delete_from_db()

        return {'message': 'Brand deleted'}


class BrandList(Resource):
    def get(self):
        return {'brands': list(map(lambda x: x.json(), BrandModel.query.all()))}