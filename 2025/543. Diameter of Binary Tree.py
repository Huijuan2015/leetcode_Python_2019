# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 最长路径有可能不经过root
        self.res = 0
        def depth(root):
            if not root:
                return 0
            left = depth(root.left) + 1
            right = depth(root.right) + 1
            self.res = max(left+right-2, self.res)
            return max(left, right)

        depth(root)
        return self.res