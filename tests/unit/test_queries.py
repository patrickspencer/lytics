# -*- coding: utf-8 -*-

import unittest
import os
import tempfile
import lytics
from sqlalchemy import create_engine, inspect, desc, exists
from sqlalchemy.orm import sessionmaker
from lytics.db.models import Expenditure
from lytics import settings, db
from lytics.db import queries

class TestQueriesModule(unittest.TestCase):

    def test_create_expenditure(self):
        """
        Should have entry in database after create_expenditure is called
        """
        # this creates the test database if it doesn't already exist
        # create_expenditure creates an expenditures and returns its id
        query_conn = queries.QueryConn(settings.DATABASE_URI)
        expenditure_id = query_conn.create_expenditure('2016-01-20','15:00',
                'This is a description',5.20,1)

        # connect to db to see if create_expenditure worked
        engine = create_engine(settings.DATABASE_URI, echo=False)
        session = sessionmaker(bind=engine)
        Session = session()
        expenditure = Session.query(Expenditure).get(expenditure_id)
        self.assertIsNotNone(expenditure)

        # delete expenditure
        Session.delete(expenditure)
        Session.commit()

    def test_expenditure_exists(self):
        """
        Should return True if expenditure exists
        """
        # this creates the test database if it doesn't already exist
        # create_expenditure creates an expenditures and returns its id
        query_conn = queries.QueryConn(settings.DATABASE_URI)
        expenditure_id = query_conn.create_expenditure('2016-01-20','15:00',
                'This is a description',5.20,1)

        # connect to db to see if create_expenditure worked
        engine = create_engine(settings.DATABASE_URI, echo=False)
        session = sessionmaker(bind=engine)
        Session = session()
        expenditure = Session.query(Expenditure).get(expenditure_id)
        self.assertTrue(query_conn.expenditure_exists(expenditure_id))

        # delete expenditure
        Session.delete(expenditure)
        Session.commit()

    def test_get_expenditure_by_id(self):
        """
        Should return True if expenditure exists
        """
        # this creates the test database if it doesn't already exist
        # create_expenditure creates an expenditures and returns its id
        query_conn = queries.QueryConn(settings.DATABASE_URI)
        expenditure_id = query_conn.create_expenditure('2016-01-20','15:00',
                'This is a description',5.20,1)

        # connect to db to see if create_expenditure worked
        engine = create_engine(settings.DATABASE_URI, echo=False)
        session = sessionmaker(bind=engine)
        Session = session()
        expenditure = Session.query(Expenditure).get(expenditure_id)
        self.assertTrue(query_conn.expenditure_exists(expenditure_id))

        # delete expenditure
        Session.delete(expenditure)
        Session.commit()
if __name__ == '__main__':
    unittest.main()
