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
        # preorder
        res = self.helper(root)
        return res[0]
    
    def helper(self, root): # return root and tail
        if not root:
            return [None, None]

        lh, lt = self.helper(root.left)
        rh, rt = self.helper(root.right)
        res = [root, root]
        root.left = None
        if lh:
            root.right = lh
            lt.right = rh
            res[1] = lt
        if rt:
            res[1] = rt
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