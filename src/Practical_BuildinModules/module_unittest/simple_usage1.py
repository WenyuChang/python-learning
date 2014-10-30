__author__ = 'wenychan'

import unittest

class SimpleTestCase(unittest.TestCase):
    def __init__(self, var):
        self.var = var

    def setUp(self):
        print 'In the setUp method...'

    def tearDown(self):
        print 'In the tearDown method...'

class DefaultTestCase(SimpleTestCase):
    def runTest(self):
        print 'DefaultTestCase - runTest'
        self.assertEqual(self.var, 'var1', 'incorrect variable...')

class AnotherTestCase(SimpleTestCase):
    def runTest(self):
        print 'AnotherTestCase - runTest'
        self.assertEqual(self.var, 'var1', 'incorrect variable...')