# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isSametree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left,t) or self.isSubtree(s.right, t)
            
    def isSametree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or  not t:
            return False
        if s.val != t.val:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            l, r = self.isSametree(s.left, t.left), self.isSametree(s.right, t.right)
            if not (l and r):
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            else:
                return l and r
            
    def isSametree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
        
        
        