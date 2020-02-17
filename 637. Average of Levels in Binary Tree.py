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
        self.res = []
        self.helper(root, 0)
        return [float(x)/y for x,y in self.res]
    
    def helper(self, root, height): #return height
        if not root:
            return
        # print root.val, height, self.res,
        if height >= len(self.res):
            self.res.append((root.val,1))
        else:
            curr, cnt = self.res[height]
            self.res[height] = (curr+root.val, cnt+1)
        # print self.res
        self.helper(root.left, height+1)
        self.helper(root.right, height+1)
        

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