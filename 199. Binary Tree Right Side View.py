# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # level travel, 每层最后一个元素
        if not root:
            return
        res = []
        level = [root]
        
        while level:
            nextLevel = []
            res.append(level[-1].val)
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        return res

recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root, 1)
        # print self.res
        return [list[-1] for list in self.res]
    
    def dfs(self, root, depth):
        if not root:
            return depth
        if depth > len(self.res):
            self.res.append([])
        self.res[depth-1].append(root.val)
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)

        