# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('-inf') #可能为负数
        self.helper(root)
        return self.ans
        
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left) 
        right = self.helper(root.right) 
        # left = 0 if not left else (left if left>0 else 0)
        # right = 0 if not right else (right if right > 0 else 0)
        l = max(0, l) #关键
        r = max(0, r)
        
        self.ans = max(self.ans, left+right+root.val)
        return max(left, right) + root.val #必须通过root才不断