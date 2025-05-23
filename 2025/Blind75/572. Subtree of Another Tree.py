# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if self.isSameTree(root, subRoot):
            return True
        if not root:
            return False
        # 递归调用 isSubtree()，而不是 isSameTree()。
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)