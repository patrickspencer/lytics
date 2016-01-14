# -*- coding: utf-8 -*-
"""
    lytics
    ~~~~~~
    Main file for lytics app.

    Usage: python lyrics.py

    :copyright: (c) 2016 by Patrick Spencer.
    :license: Apache 2.0, see LICENSE for more details.
"""

from flask import Flask
from flask import render_template
from lytics.db import queries
from lytics.api import make_api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.jinja2')

@app.route("/month/<year>/<month>")
def month_view(year, month):
    e = queries.get_expenditures_in_month(year,month)
    return render_template('expenditures/month.jinja2',
            expenditures=e)

make_api(app)

if __name__ == "__main__":
    app.config.from_object('lytics.settings.DevelopmentConfig')
    app.run(debug=True)
