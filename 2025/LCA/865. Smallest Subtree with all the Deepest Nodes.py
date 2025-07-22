# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 找一个最小子树，包含所有最深节点
        # 定义一个递归函数，返回两个值：
        # 1. 当前子树的最大深度
        # 2. 包含所有最深节点的最小子树的根节点
        def dfs(node):
            if not node:
                return (0, None)
            left, left_lca = dfs(node.left)
            right, right_lca = dfs(node.right)

            if left > right:
                return (left + 1, left_lca)
            elif left < right:
                return (right + 1, right_lca)
            else:
                return(left + 1, node)
            
        return dfs(root)[1]

same 1123. Lowest Common Ancestor of Deepest Leaves