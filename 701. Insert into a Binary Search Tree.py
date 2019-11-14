# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = TreeNode(val)
        if not root:
            return node
        curr = root
        while True:
            if curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = node
                    break
        return root
        