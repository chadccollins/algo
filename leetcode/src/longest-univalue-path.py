# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
# 
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.result = 0
        def depthfirstsearch(node):

            # return zero when passed null, which will be when we've hit the bottom of the tree
            if not node:
                return 0

            left = depthfirstsearch(node.left)
            right = depthfirstsearch(node.right)

            # if node.left isn't null, and it's value is the same as current node, add 1 to our path length
            if node.left and node.left.val == node.val:
                left += 1
            # if we're at a leaf (node.left == null) or val doesn't match, return zero
            else:
                left = 0
    
            # do the same for the right
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # store the max left + right value found
            self.result = max(self.result, left + right)

            return max(left, right)

        depthfirstsearch(root)
        return self.result
