import random
import unittest
import threading

def setUpModule():
    print 'In the setUpModule method...'

def tearDownModule():
    print 'In the tearDownModule method...'

class TestSequenceFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'In the setUpClass method...'
        print threading.current_thread
        print threading.local()
        threading.local().data = 'test'


    @classmethod
    def tearDownClass(cls):
        print 'In the tearDownClass method...'

    def setUp(self):
        print ' '*4, 'In the setUp method... id: %s' % self.id()
        self.seq = range(10)

    def tearDown(self):
        print ' '*4, 'In the tearDown method...'
        print
        self.seq = None

    def test_shuffle(self):
        print ' '*8, 'Testing Shuffle...'
        print threading.current_thread
        print threading.local()
        print threading.local().data
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        print ' '*8, 'Testing choice...'
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        print ' '*8, 'Testing Sample...'
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    # unittest.main([module[, defaultTest[, argv[, testRunner[, testLoader[, exit[, verbosity[, failfast[, catchbreak[, buffer]]]]]]]]]])
    unittest.main()

    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    # unittest.TextTestRunner(verbosity=2).run(suite)