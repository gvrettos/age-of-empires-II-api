from flask_restful import Resource
from models.structure import StructureModel


class Structure(Resource):
    def get(self, _id):
        structure = None
        if _id.isdigit():
            structure = StructureModel.find_by_id(_id)
        else:
            structure = StructureModel.find_by_name(_id)

        if structure:
            return structure.json() if len(structure) == 1 else list(map(lambda x: x.json(), structure))
        else:
            return {'message': 'Structure not found'}, 404


class StructureList(Resource):
    def get(self):
        return {'structures': list(map(lambda x: x.json(),
                StructureModel.query.all()))}