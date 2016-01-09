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
import queries

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/month/<year>/<month>")
def month_view(year, month):
    e = queries.get_expenditures_in_month(year,month)
    return render_template('expenditures/month.jinja2',
            expenditures=e)

if __name__ == "__main__":
        app.run(debug=True)
