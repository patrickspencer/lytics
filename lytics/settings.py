# -*- coding: utf-8 -*-
"""
    lytics.settings
    ~~~~~~~~~~~~~~~
    Settings file for lytics app.

    Usage:
    from lytics import settings
    settings.DATABASE_PATH
    >>> /home/lytics/db/db.sqlite3

    :copyright: (c) 2016 by Patrick Spencer.
    :license: Apache 2.0, see LICENSE for more details.
"""

from os import path

BASE_PATH = path.dirname(path.abspath(__file__))

DATABASE_DIR = path.join(BASE_PATH,'db')
DATABASE_URI = path.join(DATABASE_DIR,'db.sqlite3')
TEST_DATABASE_URI = path.join(DATABASE_DIR,'test_db.sqlite3')


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///%s' % DATABASE_URI

class ProductionConfig(Config):
    """
    Usage:
    from lytics import app
    app.config.from_object('lytics.settings.ProductionConfig')
    """
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///%s' % TEST_DATABASE_URI
