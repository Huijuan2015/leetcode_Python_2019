# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.maxDepth(root.left)+1
        r = self.maxDepth(root.right)+1
        return max(l, r)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #dfs
#         def helper(root, depth):
#             if not root:
#                 return depth
#             left = helper(root.left, depth + 1)
#             right = helper(root.right, depth + 1)
#             return max(left, right)
        
#         return helper(root, 0)
        
        #bfs
        stk = []
        level = [root]
        depth = 0
        
        while root and level:
            depth += 1
            nextLevel = []
            
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        return depth
        