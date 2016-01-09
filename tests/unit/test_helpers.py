# -*- coding: utf-8 -*-

import unittest
import os
import helpers

class TestHelpersModule(unittest.TestCase):

    def test_month_bounds(self):
        bounds = helpers.month_bounds("2015","01")
        self.assertEqual(bounds[0].strftime('%Y-%m-%d'),'2015-01-01')
        self.assertEqual(bounds[1].strftime('%Y-%m-%d'),'2015-01-31')

if __name__ == '__main__':
    unittest.main()
