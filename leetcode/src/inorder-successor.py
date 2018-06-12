# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# 
# Note: If the given node has no in-order successor in the tree, return null.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        # if p has any right tree at all, the inorder successor to p will be the minimum value in p's right subtree
        if p.right is not None:
            # start in the right sub-tree
            curr = p.right
            # and go all the way to the left
            while curr.left is not None:
                curr = curr.left
            return curr

        # if p does not have a right tree, start from the root and find p's successor
        successor = None
        while root is not None:
            # if p < root, root is a possible successor. save it and move left
            if p.val < root.val:
                successor = root
                root = root.left
            # if p > root, move right until it isn't
            elif p.val > root.val:
                root = root.right
            # else we've found p, and hopefully saved successor on the way here
            else:
                break

        return successor