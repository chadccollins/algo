#   Given two arrays, write a function to compute their intersection.
#   
#   Example:
#   Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#   
#   Note:
#   Each element in the result should appear as many times as it shows in both arrays.
#   The result can be in any order.

class Solution(object):
    
    def intersect(self, nums1, nums2):

        # first, figure out which list is bigger
        biggest = nums1 if len(nums1) > len(nums2) else nums2
        smallest = nums2 if biggest == nums1 else nums1

        result = []

        occurences = {}

        # loop thru the longest list, add the elements to the dictionary and store a value of their count
        for n in biggest:

            # if n is not already present, add it with zero
            if n not in occurences:
                occurences[n] = 0
            
            # increment the number of times we've seen n
            occurences[n] += 1
        
        # loop the the smaller list, look for intersections, consuming them as we go
        for n in smallest:

            # check that n exists and is non-zero
            # if yes, it's a new intersection on n
            if n in occurences and occurences[n] != 0:
                # so add it to the result list
                result.append(n)
                # and decrement the count
                occurences[n] -= 1
        
        return result

