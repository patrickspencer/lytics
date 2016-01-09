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

engine = create_engine('sqlite:///db.sqlite3', echo=True)
session = sessionmaker(bind=engine)
Session = session()

def get_expenditures_by_date_range(begin_date,end_date):
    """
    Returns a list of objects from the finances_expenditure table
    between two dates.

    :param begin_date: a python datetime object.
    :param end_date: a python datetime object.
    """

    return Session.query(Expenditure).filter(Expenditure.date.between(begin_date, end_date))


def get_expenditures_in_month(year, month):
    """
    Returns a list of objects from the finances_expenditure table
    for a specific month.

    :param year: four digit year as string e.g. "2016"
    :param month: two digit month as string e.g. "02"
    """
    range = helpers.month_bounds(year,month)
    return get_expenditure_by_date_range(range[0],range[1])
