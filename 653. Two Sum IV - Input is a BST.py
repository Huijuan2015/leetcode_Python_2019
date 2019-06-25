# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        st = set()
        self.helper(root,st)
        for val in st:
            target = k - val
            if target in st and target != val:
                return True
        return False
            
        
        
    def helper(self,root,st):
        if not root:
            return
        self.helper(root.left, st)
        st.add(root.val)
        self.helper(root.right,st)