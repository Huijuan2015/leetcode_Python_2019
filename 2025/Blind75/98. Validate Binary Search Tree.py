# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))
    def helper(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)