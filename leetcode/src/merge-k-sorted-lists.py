# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # simple two-list merge function, in place. O(n)
        def merge(a, b):
            """
            :type: a, b: ListNode
            :rtype: ListNode
            """
            # if a is null, return b as the merge result
            if not a:
                return b
            # same for b
            if not b:
                return a

            # if a < b recurse set a.next to the merge result continuing from a.next and b
            if (a.val < b.val):
                a.next = merge(a.next, b)
                return a
            else:
                b.next = merge(a, b.next)
                return b

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        # ok, here we go, on to the harder problem
        end = len(lists) - 1
        # we will know we're done when we have marched 'end' all the way back up the list
        while end != 0:

            # set up two pointers at opposite ends of the list of lists
            i, j = 0, end

            # move them towards each other merging while we go
            while i < j:
                # merge the first list, with the last list, and store the result
                lists[i] = merge(lists[i], lists[j])
                
                # move on to the next pair of lists
                i += 1
                j -= 1

                # when i and j collide, reset end to j, and let the outter loop keep going
                if i >= j:
                    end = j
        
        return lists[0]

        

a, b, c = ListNode(1), ListNode(4), ListNode(5)
a.next = b
b.next = c

d, e, f = ListNode(1), ListNode(3), ListNode(4)
d.next = e
e.next = f

g, h = ListNode(2), ListNode(6)
g.next = h

result = Solution().mergeKLists([a, d, g])
while (True):
    print (result.val)

    if not result.next:
        break
    else:
        result = result.next
