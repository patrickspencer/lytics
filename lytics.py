from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/month/<int:year>/<int:month>")
def month_view(year, month):
    string = "Year: %d, month: %d" % (year,month)
    return render_template('finances/expenditures_by_month.jinja2', string=string)

if __name__ == "__main__":
        app.run(debug=True)
