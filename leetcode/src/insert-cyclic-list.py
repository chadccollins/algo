# Given a node from a cyclic linked list which is sorted in ascending order,
# write a function to insert a value into the list such that it remains a cyclic sorted list.
# The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.
# 
# If there are multiple suitable places for insertion, you may choose any place to insert the new value. 
# After the insertion, the cyclic list should remain sorted.
# 
# If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node.
# Otherwise, you should return the original given node.
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
        
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """

        if head is None:
            head = Node(insertVal, None)
            head.next = head
            return head 

        # save a reference to the head, to keep us from going in circles
        curr = head
        # loop until we find the insert point

        while True:
            # first case, somewhere in the middle of this list 
            if curr.val < curr.next.val:
                # if we find a spot where insertVal is between curr and curr.next, we've found our spot 
                if curr.val <= insertVal and insertVal <= curr.next.val:
                    break
                # else, not yet, keep moving forward
                else:
                    curr = curr.next

            # second case, we're at the end of the list, now curr.next.val < curr.val
            elif curr.next.val < curr.val:
                # we can insert here if insertVal is either the highest or lowest in the list
                if curr.val <= insertVal or insertVal <= curr.next.val:
                    break
                else:
                    curr = curr.next
            # keep moving forward
            else:
                # one last case, where we have a cycle but the values are all the same
                if curr.next == head:
                    break
                curr = curr.next

        # if we're out of the loop, we've identified our insert point at curr, so insert it!
        node = Node(insertVal, curr.next)
        curr.next = node

        return head


if __name__ == "__main__":
    head = Node(3, None)
    tail = Node(3, Node(3, head))
    head.next = tail
    print (Solution().insert(head, 0))

