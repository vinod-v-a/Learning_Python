import unittest
from ops import *

class TestOps(unittest.TestCase):
    def setUp(self):
        print("from setup")
    def tearDown(self):
        print("from teardown")

    def test_add_two_int(self):
        print("from test_add_two_int")
        res = add(10, 5)
        self.assertEqual(15, res)

if __name__ == "__main__":
    unittest.main