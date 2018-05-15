class Solution(object):
    # the main func, here's where we decide which character to remove
    def validPalindrome(self, s):

        head = 0
        tail = len(s) - 1

        while head <= tail:
            a = s[head]
            b = s[tail]
            #if a equals b, we're still a palindrome, so keep iterating
            if a == b:
                head += 1
                tail -= 1
            # we're not a palindrome, so we need to test the character removal
            else:
                # either s[head] or s[tail] needs to be removed
                # first check if removing s[head] works
                if self.simplePalindrome(s[(head+1):tail+1]):
                    return True
                # then check if removing s[tail] works
                elif self.simplePalindrome(s[head:(tail)]):
                    return True
                # neither worked, return false
                else:
                    return False

        return True

    # helper function, dead simple palindrome check for substrings
    def simplePalindrome(self, s):
        head = 0
        tail = len(s) - 1

        while head <= tail:
            if not s[head] == s[tail]:
                return False
            head += 1
            tail -= 1
        
        return True

s = Solution()

print (s.validPalindrome("abc"))