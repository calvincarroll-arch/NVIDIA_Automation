import unittest

# This is the cable that plugs into our toy robot
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    
    # 1. The Normal Case
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    # 2. Edge Case: What if they send nothing?
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    # 3. Edge Case: What if there is no comma? (Testing our Safety Net!)
    def test_single_name(self):
        testcase = "Ada"
        expected = "Ada"
        self.assertEqual(rearrange_name(testcase), expected)

# The switch to turn the machine on
if __name__ == '__main__':
    unittest.main()