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
        def dfs(node):
            if not node:
                return (None, False, False) #
            
            left_lca, left_p, left_q = dfs(node.left)
            right_lca, right_p, right_q = dfs(node.right)

            found_p = left_p or right_p or node == p
            found_q = left_q or right_q or node == q

            if node == p or node == q:
                return (node, found_p, found_q)
            if left_lca and right_lca:
                return (node, found_p, found_q)
            if left_lca: # “如果在左子树中已经找到了最近公共祖先（LCA）”，就把它直接返回上去。
                return (left_lca, found_p, found_q)
            if right_lca:
                return (right_lca, found_p, found_q)

            return (None, found_p, found_q)
        
        lca, has_p, has_q = dfs(root)
        return lca if has_p and has_q else None




