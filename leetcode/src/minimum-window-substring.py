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

        # this will be useful
        A = ord('A')

        # count the characters in the input and store the counts in the array
        for c in t:
            char = ord(c) - A 
            expected[char] += 1
        
        i, count, start = 0, 0, 0

        # this will track the start of a window within which we have matched all characters
        min_window_len = len(s)
        min_window_start = 0
        # traverse s
        while i < len(s):
            # record the character found in s
            char = ord(s[i]) - A
            found[char] += 1

            # if the count of the character at s[i] <= the count of the same character in the input string, increment count
            if found[char] <= expected[char]:
                count += 1

            # if count == len(t) we have at least found very character
            if count == len(t):
                # try to find the window
                wchar = ord(s[start]) - A
                while found[wchar] > expected[wchar]:
                    # consume the character
                    found[wchar] -= 1
                    # move the start forward
                    start += 1

                # i is the current location thru s, start is the start of the window where we've found all characters
                # if the current window (start + 1 to i) is less than the min window
                if i - start + 1 < min_window_len:
                    # the reset the minimum window
                    min_window_len = i - start + 1
                    min_window_start = start
                
            # move forward in s
            i += 1

        # if we didn't find anything, return empty
        if min_window_len == len(s):
            return ""

        return s[min_window_start:min_window_start + min_window_len]
        


if __name__ == "__main__":
    print (Solution().minWindow("ADOBECODEBANC", "ABC"))