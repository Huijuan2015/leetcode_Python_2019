# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[1]

    def helper(self, root): # return height and lca
        if not root:
            return 0, None
        
        h1, lca1 = self.helper(root.left)
        h2, lca2 = self.helper(root.right)
        
        if h1 > h2:
            return h1+1, lca1
        if h1 < h2:
            return h2+1, lca2
        return h1+1, root
    