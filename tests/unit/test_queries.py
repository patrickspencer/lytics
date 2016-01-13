# -*- coding: utf-8 -*-

import unittest
import os
import tempfile
import lytics

# Set DATABASE_URI to testing database
lytics.app.config.from_object('lytics.settings.TestingConfig')


class TestQueriesModule(unittest.TestCase):

    def setup(self):
        lytics.app.config.from_object('lytics.settings.TestingConfig')


    def test_create_expenditure(self):
        """
        Should have entry in database after create_expenditure is called
        """
        # this creates the test database if it doesn't already exist
        query_conn = lytics.db.queries.QueryConn(lytics.app.config['DATABASE_URI'])
        lytics.db.queries.create_expenditure('2016-01-20','15:00','This is a decrition',5.20,1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
