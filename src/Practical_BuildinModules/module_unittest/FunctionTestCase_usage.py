__author__ = 'wenychan'

import unittest

def setUp():
    print 'In setUp method...'

def tearDown():
    print 'In tearDown method...'

def test_something():
    print 'test something...'
    import time
    time.sleep(2)

testcase = unittest.FunctionTestCase(test_something, setUp=setUp, tearDown=tearDown)
# result = unittest.TestResult()
# testcase.run(result)
# print '#'*10
# print result