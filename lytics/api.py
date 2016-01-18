# -*- coding: utf-8 -*-
"""
    api
    ~~~
    Main api declarations lytics app.

    :copyright: (c) 2016 by Patrick Spencer.
    :license: Apache 2.0, see LICENSE for more details.
"""

from flask import current_app
from flask.json import jsonify
from flask_restful import Resource, Api, reqparse
from lytics.db import queries
import lytics
from lytics.settings import DevelopementConfig

parser = reqparse.RequestParser()
parser.add_argument('date')
parser.add_argument('time')
parser.add_argument('description')
parser.add_argument('cost')
parser.add_argument('category_id')

query_conn = QueryConn(DevelopmentConfig.DATABASE_URI)

def abort_if_expenditure_does_not_exist(expenditure_id):
    if not query_conn.expenditure_exists(expenditure_id):
        abort(404, message="Expenditure {} does not exist".format(expenditure_id))

class Expenditure(Resource):
    def get(self, expenditure_id):
        abort_if_expenditure_does_not_exist(expenditure_id)
        return jsonify(expenditure=query_conn.get_expenditure_by_id(expenditure_id).serialize)

    def delete(self, expenditure_id):
        abort_if_expenditure_does_not_exist(expenditure_id)
        return query_conn.delete_expenditure_by_id(expenditure_id), 204

class ExpenditureList(Resource):
    def get(self):
        return jsonify(json_list=[i.serialize for i in queries.get_expenditures()])

    def post(self):
        args = parser.parse_args()
        return query_conn.create_expenditure(args['date'], args['time'],
                args['description'], args['cost'], args['category_id']), 201

def make_api(app):
    api = Api(app)
    api.add_resource(ExpenditureList, '/api/expenditures/')
    api.add_resource(Expenditure, '/api/expenditure/<expenditure_id>/')
    # api.add_resource(Expenditure, '/api/expenditure/<string:expenditure_id>')
