# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return 0
        leftLen = self.helper(root.left)
        rightLen =  self.helper(root.right)
        self.ans = max(self.ans, leftLen+rightLen)
        return max(leftLen, rightLen) + 1