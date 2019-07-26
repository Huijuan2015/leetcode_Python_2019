# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        self.helper(root)
        return self.res
    
    def helper(self, root): # return subtree root val
        if not root:
            return
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if (not left or left == root.val) and (not right or right == root.val):
            self.res += 1
            return root.val
        # If current tree is not univalued, the parent tree cannot be univalued either. 
        # So we return a value that the parent tree's root node can never match.
        return '#'
        