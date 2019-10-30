# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def getLevel(root, dict):
            if not root:
                return 0
            left = getLevel(root.left, dict)
            right = getLevel(root.right, dict)
            level = 1 + max(left, right)
            dict[level].append(root.val)
            return level
        
        dict = collections.defaultdict(list)
        print dict
        getLevel(root, dict)
        print dict
        res = []
        for k in sorted(dict.keys()):
            res.append(dict[k])
        return res



/// stack?