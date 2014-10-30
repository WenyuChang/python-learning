__author__ = 'wenychan'

"""
Usage:
    > nosetests -s test_um_nose_fixtures.py
    ....
    setup_module before anything in this file
    setup_class() before any methods in this class
    TestUM:setup() before each test method
    test_numbers_5_6()  <============================ actual test code
    TestUM:teardown() after each test method
    TestUM:setup() before each test method
    test_strings_b_2()  <============================ actual test code
    TestUM:teardown() after each test method
    teardown_class() after any methods in this class
    my_setup_function
    test_numbers_3_4  <============================ actual test code
    my_teardown_function
    my_setup_function
    test_strings_a_3  <============================ actual test code
    my_teardown_function
    teardown_module after everything in this file

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK
"""

"""
Test discovery:
    Name my test modules/files starting with ‘test_’.
    Name my test functions starting with ‘test_’.
    Name my test classes starting with ‘Test’.
    Name my test methods starting with ‘test_’.
    Make sure all packages with test code have an ‘init.py’ file.

"""



# ================================== code ==================================
from nose import with_setup # optional

def multiply(a, b):
    return a*b


"""
at the beginning and end of a module of test code (setup_module/teardown_module)
To get this to work, you just have to use the right naming rules.
"""
def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("setup_module before anything in this file")
def teardown_module(module):
    print ("teardown_module after everything in this file")


"""
before and after a test function call (setup_function/teardown_function)
You can use any name. You have to apply them with the ‘@with_setup’ decorator imported from nose.
You can also use direct assignment, which I’ll show in the example.
"""
def my_setup_function():
    print ("my_setup_function")

def my_teardown_function():
    print ("my_teardown_function")

@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print 'test_numbers_3_4  <============================ actual test code'
    assert multiply(3,4) == 12

@with_setup(my_setup_function, my_teardown_function)
def test_strings_a_3():
    print 'test_strings_a_3  <============================ actual test code'
    assert multiply('a',3) == 'aaa'


class TestUM:
    def __init__(self):
        pass

    """
    before and after a test method call (setup/teardown)
    To get this to work, you have to use the right name.
    """
    def setup(self):
        print ("TestUM:setup() before each test method")
    def teardown(self):
        print ("TestUM:teardown() after each test method")

    """
    at the beginning and end of a class of test methods (setup_class/teardown_class)
    To get this to work, you have to use the right naming rules, and include the ‘@classmethod’ decorator.
    """
    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")
    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")

    def test_numbers_5_6(self):
        print 'test_numbers_5_6()  <============================ actual test code'
        assert multiply(5,6) == 30

    def test_strings_b_2(self):
        print 'test_strings_b_2()  <============================ actual test code'
        assert multiply('b',2) == 'bb'