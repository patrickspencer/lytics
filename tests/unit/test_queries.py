# -*- coding: utf-8 -*-

import unittest
import os
import tempfile
import lytics

class TestQueriesModule(unittest.TestCase):

    def setup(self):
        lytics.app.config.from_object('lytics.settings.TestingConfig')
        print(lytics.app.config['DATABASE_URI'])

    def test_dbconn(self):
        """
        DBConn(DATABASE_PATH) should load a conenction to the db
        """

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
