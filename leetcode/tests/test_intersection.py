
import unittest
import src.intersection

class TestIntersection(unittest.TestCase):

    sln = src.intersection.Solution()

    def test(self):
        nums1 = [1,2,2,1]
        nums2 = [2,2]

        sln = src.intersection.Solution()
        result = sln.intersect(nums1, nums2)

        self.assertEqual([2,2], result)