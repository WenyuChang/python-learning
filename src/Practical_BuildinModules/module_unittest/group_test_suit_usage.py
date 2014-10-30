__author__ = 'wenychan'

import unittest
from simple_usage2 import get_suit1, get_suit2, get_suit3

suite1 = get_suit1()
suite2 = get_suit2()
suite3 = get_suit3()
group_test_suit = unittest.TestSuite([suite1, suite2, suite3])

group_test_suit.addTest(suite3)
group_test_suit.addTests([suite3, suite1])

group_test_suit.run()
group_test_suit.debug()