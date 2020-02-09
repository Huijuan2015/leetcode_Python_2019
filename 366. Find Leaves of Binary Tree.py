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
        self.res = []
        self.depth(root)
        return self.res
    def depth(self, root): # return depth from left to root
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        depth = max(l, r) +1
        if len(self.res) < depth:
            self.res.append([])
        self.res[depth-1].append(root.val)
        return depth

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
        #use level
        self.leaves = []
        self.getLevel(root)
        return self.leaves
    
    def getLevel(self, root): 
        if not root:
            return 0
        
        l = self.getLevel(root.left)
        r = self.getLevel(root.right)
        level = max(l,r) + 1
        if level > len(self.leaves):
            self.leaves.append([])
        self.leaves[level-1].append(root.val)
        return level
        

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