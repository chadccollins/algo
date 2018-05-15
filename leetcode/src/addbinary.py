# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

class Solution(object):

    def addBinary(self, a, b):

        result = [] 
        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        # while there are digits left in a or b
        while i >= 0 or j >= 0:
            sum = 0

            # if there's still string content in A to consume
            # AND it's a 1, add it
            if i >= 0 and a[i] == '1':
                sum += 1
            
            # same thing for B
            if j >= 0 and b[j] == '1':
                sum += 1

            # apply the carry
            sum += carry

            # sum is now either 0, 1, 2,  or 3 if carry
            if sum >= 2:
                # continue the carry into the next look
                carry = 1
            else:
                carry = 0

            # turn the value into a character and prepend it to the result            
            x = (sum % 2) + ord('0')
            c = chr(x)
            result.insert(0, c)

            # decrement our indexers and keep going
            i -= 1
            j -= 1

        # if we've exited the loop, and still have a carry, take care of it
        if carry == 1:
            result.insert(0, '1')
        
        # all done, concatenate all the letters and return
        return ''.join(result)


import sys

#a = sys.argv[1]
#b = sys.argv[2]
a = '11'
b = '1'
s = Solution()

print (s.addBinary(a, b))