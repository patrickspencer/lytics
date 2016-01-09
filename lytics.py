from flask import Flask
from flask import render_template
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import models

app = Flask(__name__)

engine = create_engine('sqlite:///db.sqlite3', echo=True)
session = sessionmaker(bind=engine)
Session = session()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/month/<int:year>/<int:month>")
def month_view(year, month):
    string = "Year: %d, month: %d" % (year,month)
    expenditures = Session.query(models.Expenditure).all()
    return render_template('finances/expenditures_by_month.jinja2',
            expenditures=expenditures)

if __name__ == "__main__":
        app.run(debug=True)
