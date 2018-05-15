import unittest
import src.ispalindrome


class TestIsPalindrome(unittest.TestCase):
    def test(self):
        self.assertFalse(src.ispalindrome.ispalindrome('abc'))
