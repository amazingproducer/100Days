import unittest
from inspect import getargspec
from tdd_fizzbuzz import FizzBuzz as fb


class FizzBuzzSetup(unittest.TestCase):
    def test_for_FizzBuzz_replacement(self):
        fb_list = fb.replace_numbers()
        self.assertEqual(fb_list[14], "FizzBuzz")

    def test_for_Buzz_replacement(self):
        fb_list = fb.replace_numbers()
        self.assertEqual(fb_list[4], "Buzz")

    def test_for_Fizz_replacement(self):
        fb_list = fb.replace_numbers()
        self.assertEqual(fb_list[2], "Fizz")


if __name__ == '__main__':
    unittest.main()
