# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path = []
        self.paths = []
        self.helper(root, sum, path)
        return self.paths
        
    def helper(self, root, sum, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and root.val == sum:
            self.paths.append(path[:])
            return
        self.helper(root.left, sum-root.val, path[:])
        self.helper(root.right, sum-root.val, path[:])
        
#          temp is just a reference, whereas temp[:] is a shallow copy of the temp array. 
# When you are doing recursive call, you want to lock the current state of the temp array,
# otherwise when you are changing the temp in the left tree, you will also change the value of 
# temp in the right subtree
        