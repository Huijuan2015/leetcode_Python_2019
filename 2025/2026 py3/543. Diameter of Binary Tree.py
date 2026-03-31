# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans
    def helper(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.ans = max(self.ans, left+right)
        return max(left, right) + 1