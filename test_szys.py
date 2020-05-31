import unittest
from szys import *
 
class TestSzYs(unittest.TestCase):
 
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    def test_add(self):
        self.assertEqual(36, add(12, 24))
        self.assertNotEqual(32, add(12, 24))
 
    def test_sub(self):
        self.assertEqual(10, sub(22, 12))
        self.assertNotEqual(12, sub(22, 12))
 
    def test_multi(self):
        self.assertEqual(6, multi(2, 3))
        self.assertNotEqual(4, multi(2, 3))
 
    def test_divide(self):
        self.assertEqual(3, divide(7, 2))
        self.assertNotEqual(3.5, divide(7, 2))
 
if __name__ == '__main__':
    unittest.main(verbosity=2)