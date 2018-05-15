class Solution(object):

    #def isNumber_simple(self, s):
        # simple number finder, only happy with 123.456
        #i = 0
        #while s[i].isdigit() and i < len(s) - 1:
            #i += 1
        #
        #if s[i] != '.'
            #return False
#
        #i += 1
#
#        while s[i].isdigit()
    
    # validate if a given string is numeric 
    def isNumber(self, s):
        # some examples:
        # "0" => true
        # " 0.1 " => true
        # "abc" => false
        # "1 a" => false
        # "2e10" => true

        # one . is allowed, two+ is not
        decimals = 0
        # one e is allowed, two are not
        e = 0

        for c in s:
            # if it's a digit, keep on truckin
            if c.isdigit():
                continue
            
            # if it's a . count it
            if c == '.':
                decimals += 1

            # if it's not a digit, or a ., it'd better be an e
            if c != '.':
                if c == 'e' or c == 'E':
                    # count the e and then it better be numbers from here on out
                    e += 1 
                else:
                    # 1234q567 is not a valid number, return False
                    return False

            if decimals > 1 or e > 1:
                return False

        return True

import sys

n = sys.argv[1]

s = Solution()

print (s.isNumber(n))