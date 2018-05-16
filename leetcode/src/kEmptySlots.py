# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

# If there isn't such day, output -1.

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # given flowers [1, 3, 2] the garden behaves like this:
        # day 0 ___
        # day 1 X__
        # day 2 X_X
        # day 3 XXX

        # first up, convert our flowers list into a days list
        # flowers [1, 3, 2] becomes days
        days = [0] * len(flowers)   # an array of 0, len(flowers) in length
        for i in xrange(len(flowers)):
            days[flowers[i] - 1] = i

        # temp result variable, set to infinity, so we can know when we've unset it
        result = float("inf")

        # an interator, and the left and right sides of the range of flowers we are looking for
        i, left, right = 0, 0, k + 1

        # move the window to the right, until we run out of days
        while right < len(days):
            if days[i] < days[left] or days[i] <= days[right]:
                if i == right:
        
        # TBD: finish figuring this one out
        
import sys

flowers = [1, 3, 2]
k = 1
s = Solution()

print (s.kEmptySlots(flowers, k))