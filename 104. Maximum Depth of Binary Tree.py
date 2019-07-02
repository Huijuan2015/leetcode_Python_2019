# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        return 1 + max(self.helper(root.right, depth), self.helper(root.left, depth))
    
    def helper(self, root, depth):
        if not root:
            return depth
        return max( self.helper(root.right, depth + 1), self.helper(root.left, depth+1))