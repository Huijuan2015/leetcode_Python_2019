# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    count = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum) 
        return self.count
        
    def helper(self, root, sum):
        if not root:
            return 0
        if root.val == sum:
            self.count += 1
        self.helper(root.right, sum - root.val)
        self.helper(root.left, sum - root.val)
        
        
        
        