__author__ = 'wenychan'


# The TestCase class provides a number of methods to check for and report failures, such as:
# assertEqual(a, b, msg=None) 	        a == b
# assertNotEqual(a, b, msg=None) 	    a != b
# assertTrue(x, msg=None) 	            bool(x) is True
# assertFalse(x, msg=None) 	            bool(x) is False
# assertIs(a, b, msg=None) 	            a is b
# assertIsNot(a, b, msg=None) 	        a is not b
# assertIsNone(x, msg=None) 	        x is None
# assertIsNotNone(x, msg=None) 	        x is not None
# assertIn(a, b, msg=None) 	            a in b
# assertNotIn(a, b, msg=None) 	        a not in b
# assertIsInstance(a, b, msg=None) 	    isinstance(a, b)
# assertNotIsInstance(a, b, msg=None) 	not isinstance(a, b)

# It is also possible to check that exceptions and warnings are raised using the following methods:
# assertRaises(exc, fun, *args, **kwds) 	        fun(*args, **kwds) raises exc
# assertRaisesRegexp(exc, r, fun, *args, **kwds) 	fun(*args, **kwds) raises exc and the message matches regex r

# There are also other methods used to perform more specific checks, such as:
# assertAlmostEqual(a, b, places=7, msg=None, delta=None) 	round(a-b, 7) == 0
# assertNotAlmostEqual(a, b, msg=None, delta=None) 	        round(a-b, 7) != 0
# assertGreater(a, b, msg=None) 	                        a > b
# assertGreaterEqual(a, b, msg=None) 	                    a >= b
# assertLess(a, b, msg=None) 	                            a < b
# assertLessEqual(a, b, msg=None) 	                        a <= b
# assertRegexpMatches(s, r, msg=None) 	                    r.search(s)
# assertNotRegexpMatches(s, r, msg=None) 	                not r.search(s)
# assertItemsEqual(a, b, msg=None) 	                        sorted(a) == sorted(b) and works with unhashable objs
# assertDictContainsSubset(a, b, msg=None) 	                all the key/value pairs in a exist in b


# The list of type-specific methods automatically used by assertEqual() are 
# summarized in the following table. Note that it’s usually not necessary to 
# invoke these methods directly.
# assertMultiLineEqual(a, b, msg=None) 	strings
# assertSequenceEqual(a, b, msg=None, seq_type=None) 	sequences
# assertListEqual(a, b, msg=None) 	    lists
# assertTupleEqual(a, b, msg=None) 	    tuples
# assertSetEqual(a, b, msg=None) 	        sets or frozensets
# assertDictEqual(a, b, msg=None) 	    dicts