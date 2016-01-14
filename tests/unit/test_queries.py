# -*- coding: utf-8 -*-

import unittest
import os
import tempfile
import lytics
from sqlalchemy import create_engine, inspect, desc, exists
from sqlalchemy.orm import sessionmaker
from lytics.db.models import Expenditure

# Set DATABASE_URI to testing database
lytics.app.config.from_object('lytics.settings.TestingConfig')

class TestQueriesModule(unittest.TestCase):

    def setup(self):
        pass

    def test_create_expenditure(self):
        """
        Should have entry in database after create_expenditure is called
        """
        # this creates the test database if it doesn't already exist
        query_conn = lytics.db.queries.QueryConn(lytics.app.config['DATABASE_URI'])
        # create_expenditure creates an expenditures and returns its id
        expenditure_id = query_conn.create_expenditure('2016-01-20','15:00',
                'This is a description',5.20,1)

        # connect to db to see if create_expenditure worked
        engine = create_engine(lytics.app.config['DATABASE_URI'], echo=False)
        session = sessionmaker(bind=engine)
        Session = session()
        expenditure = Session.query(Expenditure).get(expenditure_id)
        self.assertIsNotNone(expenditure)

        # delete expenditure
        Session.delete(expenditure)
        Session.commit()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
