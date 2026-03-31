# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
        # right min, left max

    def helper(self, root, rightMin, leftMax):
        if not root:
            return True
        if root.val <= rightMin or root.val >= leftMax:
            return False
        return self.helper(root.left, rightMin, root.val) and self.helper(root.right, root.val, leftMax)