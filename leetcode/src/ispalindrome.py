
def ispalindrome(s): 

    if s == "":
        return True

    head = 0
    tail = len(s) - 1

    while head <= tail:
        a = s[head]
        b = s[tail]

        # if it's not a letter or digit, keep moving
        if not (a.isalpha() or a.isdigit()):
            head += 1
        
        # same for b pointer, if it's not what we want, move it inward
        elif not (b.isalpha() or b.isdigit()): 
            tail -= 1 
        
        else:
            if not a.lower() == b.lower():
                return False

            head += 1
            tail -= 1

    return True

