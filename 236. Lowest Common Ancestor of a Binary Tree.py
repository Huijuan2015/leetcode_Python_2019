# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 递归函数会返回最先遇到的点
        if root in (None, p, q):
            return root
        # 会返回 p 或者 q, either
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root # 如果都找到，则父节点当前节点
        return left if left else right #如果只找到一个，说明父节点是p或者q中的一个