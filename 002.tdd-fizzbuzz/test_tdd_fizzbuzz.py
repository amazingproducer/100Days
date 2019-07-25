import unittest
from inspect import getargspec
from tdd_fizzbuzz import FizzBuzz

class FizzBuzzSetup(unittest.TestCase):
    def test_range_has_been_set(self):
        self.assertEqual(FizzBuzz.build_fb_range(), range(1,101))
    def test_upper_limit_is_greater(self):
        self.assertTrue(getargspec(FizzBuzz.build_fb_range).args[0] <
        getargspec(FizzBuzz.build_fb_range).args[1])
if __name__ == '__main__':
    unittest.main()
