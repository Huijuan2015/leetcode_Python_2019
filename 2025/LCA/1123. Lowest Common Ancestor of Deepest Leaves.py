# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (0, None)
            left, left_lca = dfs(node.left)
            right, right_lca = dfs(node.right)

            if left > right:
                return (left+1, left_lca)
            elif left < right:
                return (right + 1, right_lca)
            else:
                return (left + 1, node)
            
        return dfs(root)[1]