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
    category_id  = Column(Integer, ForeignKey(ExpenditureCategory.id), nullable=True)
    category     = relationship('ExpenditureCategory', back_populates='expenditures')

    def __repr__(self):
       return "<Expenditure(date='%s', description='%s', cost='%s')>" % (self.date, self.description, self.cost)

    @property
    def serialize(self):
       """
       Return object data in easily serializeable format
       """
       return {
           'id': self.id,
           'date': self.date.strftime("%Y-%m-%d"),
           'time': self.time.strftime("%H:%M"),
           'cost': self.cost,
           'description': self.description,
           'category_id': self.category_id,
           'category': self.category.name
       }
