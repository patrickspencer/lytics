# -*- coding: utf-8 -*-
"""
    api
    ~~~
    Main api declarations lytics app.

    :copyright: (c) 2016 by Patrick Spencer.
    :license: Apache 2.0, see LICENSE for more details.
"""

from flask.json import jsonify
from flask_restful import Resource, Api, reqparse
import queries

parser = reqparse.RequestParser()
parser.add_argument('date')

class Expenditure(Resource):
    def get(self, expenditure_id):
        return jsonify(expenditure=queries.get_expenditure_by_id(expenditure_id).serialize)

class ExpenditureList(Resource):
    def get(self):
        return jsonify(json_list=[i.serialize for i in queries.get_all_expenditures()])

    def post(self):
        args = parser.parse_args()
        return args['date'], 201
        # queries.create_expenditure(date, time, description, cost, category_id)

def make_api(app):
    api = Api(app)
    api.add_resource(ExpenditureList, '/api/expenditures/')
    api.add_resource(Expenditure, '/api/expenditure/<expenditure_id>/')
    # api.add_resource(Expenditure, '/api/expenditure/<string:expenditure_id>')
