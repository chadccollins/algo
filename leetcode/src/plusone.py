
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# 
# Example 1:
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = 0
        power = 1

        # run thru the digits, backwards and add up the number by increasing powers of 10
        for i in reversed(range(0, len(digits))):
            n += (digits[i] * power)
            power *= 10
        
        # add the 1
        n += 1

        result = []
        # now split it up again to put it back into an array
        for digit in str(n):
            result.append(int(digit))

        return result 

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # go thru the digits, backwards, add one and carry if needed
        for i in reversed(range(0, len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        # if we get here, we're looking at a 9999... type number and we've turned it into 0000...
        # finish the job by adding 1 in a strange way: 1 + 0000... + 0 
        digits[0] = 1
        digits.append(0)
        return digits

print (Solution().plusOne([1,2,3]))
print (Solution().plusOne([2,3]))
print (Solution().plusOne([2,3,4,5]))
print (Solution().plusOne2([1,2,3]))
print (Solution().plusOne2([2,3]))
print (Solution().plusOne2([2,3,4,5]))