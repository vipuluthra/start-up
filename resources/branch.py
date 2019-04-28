from flask_restful import Resource
from models.branch import BranchModel


class Branch(Resource):
        parser = reqparse.RequestParser()
        parser.add_argument('brand_id',
                        type=int,
                        required=True,
                        help="Every branch needs a brand_id."

    def get(self, id):
        branch = BranchModel.find_by_id(id)
        if store:
            return branch.json()
        return {'message': 'Branch not found'}, 404                   

    def post(self, id):
        if BranchModel.find_by_id(id):
            return {'message': "A branch with id '{}' already exists.".format(id)}, 400

        branch = BranchModel(id)
        try:
            branch.save_to_db()
        except:
            return {"message": "An error occurred creating the branch."}, 500

        return branch.json(), 201

    def delete(self, id):
        branch = BranchModel.find_by_id(id)
        if branch:
            branch.delete_from_db()

        return {'message': 'Branch deleted'}


class BranchList(Resource):
    def get(self):
        return {'branches': list(map(lambda x: x.json(), BranchModel.query.all()))}