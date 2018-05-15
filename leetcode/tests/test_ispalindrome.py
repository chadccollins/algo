import unittest
import src.ispalindrome


class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(src.ispalindrome.ispalindrome('abc'))


if __name__ == '__main__':
    unittest.main()