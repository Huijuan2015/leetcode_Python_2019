# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # depth diff smaller than 1
        if not root:
            return True
        
        l = self.depth(root.left, 1)
        r = self.depth(root.right, 1)
        if abs(l-r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self, root, depth):
        if not root:
            return depth
        l = self.depth(root.left, depth+1)
        r = self.depth(root.right, depth+1)
        return max(l, r)