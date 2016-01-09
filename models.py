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


