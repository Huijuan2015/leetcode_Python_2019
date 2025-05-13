# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0
        self.depth(root)
        return self.res
    
    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left) + 1
        r =  self.depth(root.right) + 1
        self.res = max(l+r-2, self.res)
        return max(l, r)