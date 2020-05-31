import unittest
from test_szys import TestSzYs
 
if __name__ == '__main__':
    suite = unittest.TestSuite()
 
    tests = [TestSzYs("test_add"), TestSzYs("test_sub"), TestSzYs("test_multi"),TestSzYs("test_divide")]
    suite.addTests(tests)
 
    with open('UnittestResult.txt.txt', 'a') as  f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

