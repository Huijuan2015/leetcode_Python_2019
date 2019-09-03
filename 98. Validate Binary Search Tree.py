# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, root, lower_bound, upper_bound):
        if not root:
            return True
        if root.val <= lower_bound or root.val >= upper_bound:
            return False
        
        return self.helper(root.left, lower_bound, root.val) and self.helper(root.right, root.val, upper_bound)
    