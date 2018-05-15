import unittest
import src.movezeros

class TestMoveZeroes(unittest.TestCase):

    sln = src.movezeros.Solution()

    def test(self):
        sln = src.movezeros.Solution()
        nums = [0,1,0,3,12]
        actual = sln.moveZeroes(nums)

        self.assertEqual([1,3,12,0,0], nums)