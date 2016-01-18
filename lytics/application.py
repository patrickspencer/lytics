from flask import Flask
from lytics import settings
from flask_restful import Resource, Api, reqparse
from lytics.db import queries
from lytics.api import ExpenditureList, Expenditure

def create_app(config_filename):
    """
    Returns a Flask app given a configuration object

    :param config_object: a string which points to a class holding the
    configuration settings
    """
    app = Flask(__name__)
    app.config.from_object(settings.DevelopmentConfig)

    from lytics.routes import main

    app.register_blueprint(main)
    api = Api(app)
    api.add_resource(ExpenditureList, '/api/expenditures/')
    api.add_resource(Expenditure, '/api/expenditure/<expenditure_id>/')

    return app
