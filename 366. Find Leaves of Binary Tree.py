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
        with dict
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

without dict
        self.leaves = []
        
        def getLevel(root, leaves):
            if not root:
                return 0
            
            l = getLevel(root.left, leaves)
            r = getLevel(root.right, leaves)
            level = max(l, r) + 1 # root level
            if level > len(leaves):
                leaves.append([])
            leaves[level-1].append(root.val)
            return level
        getLevel(root, self.leaves)
        return self.leaves

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
        leaves = []
        
        def helper(root, leaf): #以root为根，找root下的叶子
            if not root:
                return
            if not root.right and not root.left:
                leaf.append(root.val)
                return #返回None,= 删除叶子
            root.left = helper(root.left, leaf)
            root.right = helper(root.right, leaf)
            return root #?
        
        while root:
            print root.val
            leaf = []
            root = helper(root, leaf)
            leaves.append(leaf)
        return leaves

/// stack?