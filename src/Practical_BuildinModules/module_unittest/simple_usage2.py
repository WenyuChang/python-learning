__author__ = 'wenychan'

import unittest

class SimpleTestCase(unittest.TestCase):
    def __init__(self, var='var1'):
        self.var = var

    @classmethod
    def setUpClass(cls):
        print 'In the setUpClass method...'

    @classmethod
    def tearDownClass(cls):
        print 'In the tearDownClass method...'

    def setUp(self):
        print 'In the setUp method...'

    def tearDown(self):
        print 'In the tearDown method...'


    def test_default(self):
        print 'DefaultTestCase - runTest'
        self.assertEqual(self.var, 'var1', 'incorrect variable...')

    def test_another(self):
        print 'AnotherTestCase - runTest'
        self.assertEqual(self.var, 'var1', 'incorrect variable...')


def get_suit1():
    # approach 1 to form test suit
    default_test_case = SimpleTestCase('var1')
    another_test_case = SimpleTestCase('var2')
    test_suit = unittest.TestSuite()
    test_suit.addTest(default_test_case)
    test_suit.addTest(another_test_case)
    return test_suit

def get_suit2():
    # approach 2 to form test suit
    tests = ['var1', 'var2']
    test_suit = unittest.TestSuite(map(SimpleTestCase, tests))
    return test_suit


def get_suit3():
    # approach 3 to form test suit
    test_suit = unittest.TestLoader().loadTestsFromTestCase(SimpleTestCase)
    return test_suit






