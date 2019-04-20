from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )

    
    def get(self, name):                            #this endpoint is being used to retreive brand from the database
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    


class ItemList(Resource):                #this endpoint will be used to retreive all the brands at once by clicking the tab 'brands near me'
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}