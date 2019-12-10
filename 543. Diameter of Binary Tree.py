# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return 0
        leftLen = self.helper(root.left)
        rightLen =  self.helper(root.right)
        self.ans = max(self.ans, leftLen+rightLen)
        return max(leftLen, rightLen) + 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # longest of left + right
        # longest of left or right only
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root): # return root depth, calculat path length through current root
        if not root:
            return 0
        l = self.helper(root.left) + 1
        r = self.helper(root.right) + 1
        self.res =  max(l+r-2, self.res)
        return max(l, r)