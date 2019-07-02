"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        ht = self.helper(root)
        return ht[0]
    
    # return [min, max]
    def helper(self, root):
        if not root:
            return [None,None]
        left = self.helper(root.left) #[min, max]
        right = self.helper(root.right)
        ret = [None for i in xrange(2)]
        
        if left[1]:
            left[1].right = root
            root.left = left[1]
            ret[0] = left[0]
        else:
            ret[0] = root
        if right[0]:
            root.right = right[0]
            right[0].left = root
            ret[1] = right[1]
        else:
            ret[1] = root
        
        ret[0].left = ret[1]
        ret[1].right = ret[0]
        
        return ret
        