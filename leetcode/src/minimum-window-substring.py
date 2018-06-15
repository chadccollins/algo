# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# 
# Example:
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
# 
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # build a list of the count of letters
        expected = [0 for i in range(26)]
        found = [0 for i in range(26)]

        # count the characters in the input and store the counts in the array
        for char in t:
            expected[ord(char) - ord('A')] += 1
        
        i, count = 0, 0

        while i < len(s):
            # record the character found in s
            char = ord(s[i]) - ord('A')
            found[char] += 1

            # if the count of the character at s[i] <= the count of the same character in the input string, increment count
            if found[char] <= expected[char]:
                count += 1

            # if count == len(t) we have consumed every character
            if count == len(t):
                
            # move forward in s
            i += 1