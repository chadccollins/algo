# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # first up, the base case
        if root is None:
            return

        # recursively invert the left and the right
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        # then invert the root!
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # return our result
        return root