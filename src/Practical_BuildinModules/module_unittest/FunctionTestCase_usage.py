__author__ = 'wenychan'

import unittest

def setUp():
    print 'In setUp method...'

def tearDown():
    print 'In tearDown method...'

def test_something():
    print 'test something...'


testcase = unittest.FunctionTestCase(test_something, setUp=setUp, tearDown=tearDown)