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
        
        i, count = 0, 0

        # this will track the start of a window within which we have matched all characters
        window_start = 0
        min_window_len = -1
        min_window_start = -1
        # traverse s
        while i < len(s):
            # record the character found in s
            char = ord(s[i]) - A
            found[char] += 1

            # if the count of the character at s[i] <= the count of the same character in the input string, increment count
            if found[char] <= expected[char]:
                count += 1

            # if count == len(t) we have consumed every character
            if count == len(t):
                # try to find the window
                wchar = ord(s[window_start]) - A
                while expected[wchar] == 0 or found[wchar] > expected[wchar]:
                    # consume the character
                    found[wchar] -= 1
                    # move the start forward
                    window_start += 1

                window_len = i - window_start + 1
                # if we havent yet found a window, or the one we just found is smaller, save it
                if min_window_len < 0 or min_window_len > window_len:
                    min_window_len = window_len 
                    min_window_start = window_start
                
            # move forward in s
            i += 1

        # if we didn't find anything, return empty
        if min_window_len == -1:
            return ""

        return s[min_window_start:min_window_start + min_window_len]
        


if __name__ == "__main__":
    print (Solution().minWindow("ADOBECODEBANC", "ABC"))