#   Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#   
#   Note:
#   The solution set must not contain duplicate triplets.
#   
#   Example:
#   Given array nums = [-1, 0, 1, 2, -1, -4],
#   
#   A solution set is:
#   [
#     [-1, 0, 1],
#     [-1, -1, 2]
#   ]

class Solution(object):

    def threeSum(self, nums):

        result = []
        # sort the inpur array first, that'll allow us to skip over duplicates
        nums.sort()

        i = 0
        end = len(nums) - 1

        while i < end:
            # pick the first digit at i
            a = nums[i]
            # set up two cursors: j at the next index, k at the end
            j = i + 1
            k = end

            # march j and k towards each other
            while j < k:
                # pick the second and third digits.
                b = nums[j]
                c = nums[k]

                # add them up
                sum = a + b + c

                #if the sum is zero, we've found one
                if sum == 0:
                    result.append([a, b, c])

                # if it's less than zero, we should move j forward until we find a new number
                if sum <= 0:
                    while nums[j] == b and j < k:
                        j += 1

                # and the opposite if it's more than zero, move k backards until a new, smaller number
                if sum >= 0:
                    while nums[k] == c and j < k:
                        k -= 1
                
            # after the while loop, j and k have collided, so it's time to move i forward and try again
            # skip i ahead with the same strategy, so we don't need to consider anything where nums[i] is the same as before
            while nums[i] == a and i < end:
                i += 1
        
        return result


s = Solution()

print (s.threeSum([-1, 0, 1, 2, -1, 4]))