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
            return Node(None, None)

        # save a reference to the head, to keep us from going in circles
        curr = head

        # loop thru the list until we return to where we started
        while curr.next is not None and curr.next != head:
            # find the position to insert
            if insertVal <= curr.val:
                # insert the node by creating a new node pointed at the current node
                node = Node(insertVal, curr)
                # wedge it in between the two nodes
                curr = node
                # we're done, bail out
                return curr
            else:
                # move forward in the list
                curr = curr.next
        
        return head

if __name__ == "__main__":
    head = Node(3, None)
    tail = Node(3, Node(3, Node(4, Node(5, head))))
    head.next = tail
    print (Solution().insert(head, 0))

