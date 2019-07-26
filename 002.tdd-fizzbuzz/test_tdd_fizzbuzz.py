import unittest
from inspect import getargspec
from tdd_fizzbuzz import FizzBuzz as fb

class FizzBuzzSetup(unittest.TestCase):
    def test_range_has_been_set(self):
        fb_list = fb.replace_numbers()
        self.assertEqual(fb_list[14], "FizzBuzz")
if __name__ == '__main__':
    unittest.main()
