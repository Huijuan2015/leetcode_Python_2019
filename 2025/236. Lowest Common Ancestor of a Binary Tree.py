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
    #     	•	如果当前节点就是 p 或 q，就返回当前节点
	# •	向左子树和右子树递归找 p 和 q
	# •	有三种情况：
	# 1.	左右都找到了 ⇒ 当前节点就是最近公共祖先
	# 2.	只在一边找到了 ⇒ 返回那边的值
	# 3.	都没找到 ⇒ 返回 None
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right