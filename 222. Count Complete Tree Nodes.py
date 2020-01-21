O(lgn*lgn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        if l==r: # l满了，r的左边满了
            return pow(2, l) + self.countNodes(root.right)
        else:
            return pow(2, r) + self.countNodes(root.left)
        
    def getDepth(self, root):
        if not root:
            return 0
        return 1+self.getDepth(root.left)
        
O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.cnt(root)
        
    def cnt(self, root):
        if not root:
            return 0
        return self.cnt(root.left) + self.cnt(root.right) + 1