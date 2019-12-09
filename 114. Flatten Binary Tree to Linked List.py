recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        return self.helper(root)[0]
    def helper(self, root): #leftmost, rightmost
        if not root:
            return [None, None]
        res = [root, root]
        left = self.helper(root.left)
        right = self.helper(root.right)
        在左右存在的时候考虑链接，并更新最左，最右
        if left[0]: 
            root.right = left[0]
            root.left = None
            res[1] = left[1]
        if right[0]:
            if left[1]:
                left[1].right = right[0]
            else:
                root.right = right[0]
            res[1] = right[1]
        return res

        
        # right_left, right_right = self.helper(root.right)
        return res

iterative
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
            
        return root