from flask_restful import Resource
from models.unit import UnitModel


class Unit(Resource):
    def get(self, _id):
        unit = None
        if _id.isdigit():
            unit = UnitModel.find_by_id(_id)
        else:
            unit = UnitModel.find_by_name(_id)
        if unit:
            return unit.json()
        return {'message': 'Unit not found'}, 404


class UnitList(Resource):
    def get(self):
        return {'units': list(map(lambda x: x.json(),
                UnitModel.query.all()))}