__author__ = 'wenychan'

"""
Usage:
    > py.test -s test_um_pytest_fixtures.py
    ============================= test session starts ==============================
    platform win32 -- Python 2.7.3 -- pytest-2.2.4
    collecting ... collected 4 items

    test_um_pytest_fixtures.py ....

    =========================== 4 passed in 0.07 seconds ===========================
    setup_module      module:test_um_pytest_fixtures
    setup_function    function:test_numbers_3_4
    test_numbers_3_4  <============================ actual test code
    teardown_function function:test_numbers_3_4
    setup_function    function:test_strings_a_3
    test_strings_a_3  <============================ actual test code
    teardown_function function:test_strings_a_3
    setup_class       class:TestUM
    setup_method      method:test_numbers_5_6
    setup             class:TestStuff
    test_numbers_5_6  <============================ actual test code
    teardown          class:TestStuff
    teardown_method   method:test_numbers_5_6
    setup_method      method:test_strings_b_2
    setup             class:TestStuff
    test_strings_b_2  <============================ actual test code
    teardown          class:TestStuff
    teardown_method   method:test_strings_b_2
    teardown_class    class:TestUM
    teardown_module   module:test_um_pytest_fixtures
"""

"""
Test discovery:
    Name my test modules/files starting with ‘test_’.
    Name my test functions starting with ‘test_’.
    Name my test classes starting with ‘Test’.
    Name my test methods starting with ‘test_’.
    Make sure all packages with test code have an ‘init.py’ file.
"""


def multiply(a, b):
    return a*b

def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)

def test_numbers_3_4():
    print 'test_numbers_3_4  <============================ actual test code'
    assert multiply(3,4) == 12

def test_strings_a_3():
    print 'test_strings_a_3  <============================ actual test code'
    assert multiply('a',3) == 'aaa'


class TestUM:

    def setup(self):
        print ("setup             class:TestStuff")

    def teardown(self):
        print ("teardown          class:TestStuff")

    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)

    def test_numbers_5_6(self):
        print 'test_numbers_5_6  <============================ actual test code'
        assert multiply(5,6) == 30

    def test_strings_b_2(self):
        print 'test_strings_b_2  <============================ actual test code'
        assert multiply('b',2) == 'bb'