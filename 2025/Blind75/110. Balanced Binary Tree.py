# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        leftH = self.depth(root.left, 1)
        rightH = self.depth(root.right, 1)
        if abs(leftH-rightH) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, root, height):
        if not root:
            return height
        left = self.depth(root.left, height+1)
        right = self.depth(root.right, height+1)
        return (max(left, right))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.res = True
        self.helper(root)
        return self.res

      
    def helper(self, root,):
        if not root:
            return 0
        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1
        if abs(left-right) > 1:
            self.res = False
        return (max(left, right))