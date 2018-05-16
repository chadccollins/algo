# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# For example, with A = "abcd" and B = "cdabcdab".

# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

# Note:
# The length of A and B will be between 1 and 10000.

import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        # find the minimum number of repetitions of A that will potentially contain B based in the length of B
        min = int(math.ceil(float(len(B)) / len(A)))

        # if there is a solution, it is either:
        # exact: min * A  e.g. 'ab' 'abab'
        # or substring: (min + 1) * A  e.g. 'abc' 'cab'
        # or a wrap: (min + 2) * A e.g. 'abcd' 'cdabcdab'
        for i in range(2):
            if B in (A * (min + i)):
                return min + i

        # or it's not a match at all :(
        return -1


import sys

a = 'abababaaba'
b = 'aabaaba'
s = Solution()

print (s.repeatedStringMatch(a, b))