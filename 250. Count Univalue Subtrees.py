# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.isUniVal(root)
        return self.count
    //check if its Unival
    def isUniVal(self, root):
        if not root:
            return True
        l = self.isUniVal(root.left) 
        r = self.isUniVal(root.right) 
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False






# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        self.helper(root)
        return self.res
    
    def helper(self, root): # return subtree root val
        if not root:
            return
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if (not left or left == root.val) and (not right or right == root.val):
            self.res += 1
            return root.val
        # If current tree is not univalued, the parent tree cannot be univalued either. 
        # So we return a value that the parent tree's root node can never match.
        return '#'
        