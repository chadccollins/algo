# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# Example:
# 
# Input:  n = 2
# Output: ["11","69","88","96"]


class Solution(object):

    strobes = { '0': '0', '1': '1', '6':'9', '8':'8', '9': '6'}

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        