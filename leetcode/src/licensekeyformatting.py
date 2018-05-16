
# You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.
# 
# Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
# 
# Given a non-empty string S and a number K, format the string according to the rules described above.

# Examples:
# Input: S = "5F3Z-2e-9-w", K = 4
# Output: "5F3Z-2E9W"
# 
# Input: S = "2-5g-3-J", K = 2
# Output: "2-5G-3J"

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = []

        # loop over S from the last character moving backwards
        for i in reversed(range(len(S))):
            # if we are at a '-' keep moving
            if S[i] == '-':
                continue
            # figure out if it's time to add a '-' 
            # ex: result = [2,3], K = 2
            # 2 % (2 + 1) = 2
            if len(result) % (K + 1) == K:
                #result.insert(0, '-') # this seems too slow, so build the string backwards and reverse it at the end
                result += '-'
            
            # prepend the character at i
            # result.insert(0, S[i].upper()) seems too slow
            result += S[i]

        # return the result array joined up as a new license key
        return ''.join(reversed(result)).upper()

S = "2-5g-3-J"
K = 2

print (Solution().licenseKeyFormatting(S, K))