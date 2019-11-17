# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
Time: O(N) | Space: O(size of return array + size of queue) -> Worst Case O(2N)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # stack
        ret = []
        level = [root] if root else []
        
        while level:
            currNodes = []
            nextLevel = []

            for node in level:
                currNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currNodes)
            level = nextLevel
        return ret
        


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root, 1)
        return self.res
    
    def dfs(self, root, depth):
        if not root:
            return
        if depth > len(self.res):
            self.res.append([])
        self.res[depth-1].append(root.val)
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)