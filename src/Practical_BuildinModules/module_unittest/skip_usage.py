__author__ = 'wenychan'

import unittest

@unittest.skip("showing class skipping")
class SimpleTestCase(unittest.TestCase):
    def __init__(self, var='var1'):
        self.var = var

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

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        print 'This will never occurred...'

    @unittest.skipIf(1 <= 2, "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(1 < 2, "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    def skip_my_decorator(obj, attr):
        if hasattr(obj, attr):
            return lambda func: func
        return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
    @skip_my_decorator(1, int)
    def test_my_skip_decorator(self):
        print '...'
