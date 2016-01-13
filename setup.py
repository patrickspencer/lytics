#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup

readme = open('README.md').read()

setup(
    name = 'lytics',
    version = '0.3',
    description = "A webapp for keeping track of expenditures",
    long_description = readme,
    author = "Patrick Spencer",
    author_email = "pkspenc@gmail.com",
    url = "http://github.com/patrickspencer/lytics",
    py_modules = ['lytics'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.4'
    ]
)
