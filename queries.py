# -*- coding: utf-8 -*-
"""
    queries
    ~~~~~~~
    A collection of database queries

    :copyright: (c) 2016 by Patrick Spencer.
    :license: Apache 2.0, see LICENSE for more details.
"""

from models import Expenditure
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import helpers
from datetime import datetime

engine = create_engine('sqlite:///db.sqlite3', echo=False)
session = sessionmaker(bind=engine)
Session = session()

def get_expenditures_by_date_range(begin_date,end_date):
    """
    Returns a list of objects from the finances_expenditure table
    between two dates.

    :param begin_date: a python datetime object.
    :param end_date: a python datetime object.
    """

    begin = begin_date.strftime('%Y-%m-%d')
    end = end_date.strftime('%Y-%m-%d')
    return Session.execute("SELECT * FROM finances_expenditure WHERE date BETWEEN :begin and :end",{"begin": begin, "end": end})


def get_expenditures_in_month(year, month):
    """
    Returns a list of objects from the finances_expenditure table
    for a specific month.

    :param year: four digit year as string e.g. "2016"
    :param month: two digit month as string e.g. "02"
    """
    range = helpers.month_bounds(year,month)
    return get_expenditures_by_date_range(range[0],range[1])

def create_expenditure(date, time, description, cost, category_id):
    """
    Create a new expenditure

    :param date: string of the form "2015-03-20"
    :param time: string of the form "17:00". No seconds.
    :param description: string
    :param cost: floating point number
    :param category_id: integer
    """

    # sqlalchemy only accepts python date and time objects
    pydate = datetime.strptime(date,"%Y-%m-%d").date()
    pytime = datetime.strptime(time,"%H:%M").time()

    expenditure = Expenditure(date=pydate, time=pytime, description=description,
                              cost=cost, category_id=category_id)
    Session.add(expenditure)
    Session.flush()
    Session.commit()
    return expenditure.id

def get_all_expenditures():
    """
    Return a list of all expenditures
    """
    return Session.query(Expenditure).all()

def get_expenditure_by_id(expenditure_id):
    """
    Return an expenditure with the given id

    :param expenditure_id: integer
    """
    return Session.query(Expenditure).get(expenditure_id)

