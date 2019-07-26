"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        currLevel = [root]
        
        while currLevel: # 1 level
            nextLevel = []
            for i in xrange(len(currLevel)):
                if i < len(currLevel) - 1:
                    currLevel[i].next = currLevel[i+1]
                if currLevel[i].left:
                    nextLevel.append(currLevel[i].left)
                if currLevel[i].right:
                    nextLevel.append(currLevel[i].right) 
            currLevel = nextLevel
        return root
            

                        
                        