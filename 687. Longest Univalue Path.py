# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.find(root)
        return self.count
    
    def find(self, root):
        if not root:
            return 0
        right = self.find(root.right)
        left = self.find(root.left)
        
        right =  right+1 if root.right and root.right.val == root.val else 0
        left = left+1 if root.left and root.left.val == root.val else 0
        
        self.count =  max(self.count, right+left)
        return max(right, left)