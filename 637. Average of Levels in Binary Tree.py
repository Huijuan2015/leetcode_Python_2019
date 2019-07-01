# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        level = [root]
        
        while root and level:
            currentSum = 0
            nextLevel = []
            count = 0
            for node in level:
                currentSum += node.val
                count += 1
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentSum/float(count))
            level = nextLevel
        return ret