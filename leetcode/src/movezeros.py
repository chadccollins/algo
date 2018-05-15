#   Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#   
#   Example:
#   
#   Input: [0,1,0,3,12]
#   Output: [1,3,12,0,0]
#   Note:
#   
#   You must do this in-place without making a copy of the array.
#   Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):

        # keep track of the last place we wrote a non zero
        nonZeroIndex = 0

        for i in range(0, len(nums)):
            # move the nonzero up, and keep track of the index
            if nums[i] != 0:
                temp = nums[nonZeroIndex]
                nums[nonZeroIndex] = nums[i]
                nums[i] = temp
                nonZeroIndex += 1