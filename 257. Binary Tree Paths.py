# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return
        self.res = []
        self.findPath(root, str(root.val))
        return self.res
        
    def findPath(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            self.res.append(path)
            return
        # 剪枝条件 只有有左孩子时才继续path
        if root.left:
            self.findPath(root.left, path+'->'+str(root.left.val))
        if root.right:
            self.findPath(root.right, path+'->'+str(root.right.val))
        
        