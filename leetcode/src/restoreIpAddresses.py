

class Solution:

    def restoreIpAddresses(self, s):

        result = []
        self.restoreIpAddressesRecursive(s, 0, "", 0, result)
        return result
    
    def restoreIpAddressesRecursive(self, s, start, current, dots, result):

        # we will know we're done recursing when we've hit the end of the string and dots > 3
        if start == len(s) and dots > 3:
            ip = current
            result.append(ip)
        # else, we're not done, so we need to find the next octet
        else:
            # from s[start] to s[start + 3] add valid octets, then recurse to move on
            for i in range(start, start + 3):
                # as long as we're still inside the string, and the next octet of i length is valid, add it and keep recursing
                if i < len(s) and self.isValid(s[start:i + 1]):
                    # append the octet
                    current += s[start:i + 1] + '.'
                    # count the dot
                    dots += 1
                    # recurse, starting from i + 1, 
                    self.restoreIpAddressesRecursive(s, i + 1, current, dots, result)

    def isValid(self, s):
        # if it's empty, it's not valid
        if len(s) == 0:
            return False
        
        # '0' is valid, '01' is not valid
        if s[0] == '0' and s != "0":
            return False

        # if it's under 256, it's good
        return int(s) <= 255