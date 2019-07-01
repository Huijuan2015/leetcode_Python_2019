# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level = [root]
        levelCount = 0
        
        while root and level:
            currentNodes = []
            nextLevel = []
            levelCount += 1
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if levelCount%2 != 0:
                ret.append(currentNodes)
            else:
                ret.append(currentNodes[::-1])
            level = nextLevel   
        return ret