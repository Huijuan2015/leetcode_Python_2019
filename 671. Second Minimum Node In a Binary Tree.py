# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('inf')
        
        def helper(node):
            if not node:
                return 
            if root.val < node.val and node.val < self.res:
                self.res = node.val 
            helper(node.right)
            helper(node.left)
            
        helper(root)
        return -1 if self.res == float('inf') else self.res
        
            
            