# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~
    Model definitions and class methods

    :copyright: (c) 2016 by Patrick Spencer.
    :license: Apache 2.0, see LICENSE for more details.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, Date, Time, \
        String, ForeignKey, Float

Base = declarative_base()

class ExpenditureCategory(Base):
    __tablename__ = 'finances_category'

    id           = Column(Integer, primary_key=True)
    name         = Column(String)

    def __repr__(self):
       return "<User(username='%s')>" % (self.username)

class Expenditure(Base):
    __tablename__ = 'finances_expenditure'

    id           = Column(Integer, primary_key=True)
    date         = Column(Date)
    time         = Column(Time)
    description  = Column(String)
    cost         = Column(Float)
    category_id  = Column(Integer, ForeignKey(ExpenditureCategory.id), nullable=True)

    def __repr__(self):
       return "<User(date='%s', description='%s', cost='%s')>" % (self.date, self.description, self.cost)

    def month_bounds(self, year, month):
        """
        Returns a tuple of datetime objects (month_start,month_end) given a year and month.
        Both params are strings because we want month to be a two digit month representation
        and python doesn't handle leading zeros in integers as we want.

        :param year: four digit year as a string e.g. "2016"
        :param month: 2 digit month as a string e.g. 2 for February, 11 for November
        """
        year = int(year)
        month = int(month)
        month_start = datetime.strptime('%s,%s,1' % (year, month),'%Y,%m,%d')
        # days_in_month returns a tuple(weekday, days) where
        # weekday is the eekday the month starts on and days is the number of days in the month
        days_in_month = calendar.monthrange(year,month)
        month_end = month_start + timedelta(days=days_in_month[1]-1)
        return (month_start, month_end)
