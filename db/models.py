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
from sqlalchemy.orm import relationship

Base = declarative_base()

class ExpenditureCategory(Base):
    __tablename__ = 'finances_category'

    id           = Column(Integer, primary_key=True)
    name         = Column(String)
    description  = Column(String)
    expenditures = relationship('Expenditure', back_populates='category')

    def __repr__(self):
       return "<ExpenditureCategory(name='%s')>" % (self.name)

class Expenditure(Base):
    __tablename__ = 'finances_expenditure'

    id           = Column(Integer, primary_key=True)
    date         = Column(Date)
    time         = Column(Time)
    description  = Column(String)
    cost         = Column(Float)
    category_id  = Column(Integer, ForeignKey(ExpenditureCategory.id))
    category     = relationship('ExpenditureCategory', back_populates='expenditures')

    def __repr__(self):
       return "<Expenditure(date='%s', description='%s', cost='%s')>" % (self.date, self.description, self.cost)

    def _get_category_name(self):
        """
        Check to see if self.category is None
        """
        if self.category:
            return self.category.name
        else:
            return None

    def _get_date(self):
        """
        Must check to see if date is None
        """
        if self.date:
            return self.date.strftime("%Y-%m-%d")
        else:
            return None

    def _get_time(self):
        """
        Must check to see if time is None
        """
        if self.time:
            return self.time.strftime("%H:%M")
        else:
            return None

    @property
    def serialize(self):
       """
       Return object data in easily serializeable format
       """
       return {
           'id': self.id,
           'date': self._get_date(),
           'time': self._get_time(),
           'cost': self.cost,
           'description': self.description,
           'category_id': self.category_id,
           'category': self._get_category_name()
       }

