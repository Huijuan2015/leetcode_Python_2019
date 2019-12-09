# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 
        mp = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0))
        res = []
        
        while q:
            node, depth = q.popleft()
            mp[depth].append(node.val)
            if node.left:
                q.append((node.left, depth-1))
            if node.right:
                q.append((node.right, depth+1))
        for k in sorted(mp.keys()):
            res.append(mp[k])
        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        self.mp = defaultdict(list)
        self.leftmost, self.rightmost = 0, 0
        self.dfs(root, 0, 0)
        res = []
        
        for i in range(self.leftmost+1, self.rightmost):
            res.append([pair[0] for pair in sorted(self.mp[i], key= lambda x: x[1])])
        return res
        
    def dfs(self, root, width, count):
        self.leftmost = min(self.leftmost, width)
        self.rightmost = max(self.rightmost, width)
        if not root:
            return
        self.mp[width].append((root.val, count))
        self.dfs(root.left, width-1, count+1)
        self.dfs(root.right, width+1, count+1)
        
        
        

BFS, level traversal, keep leftmost, rightmost and mp for width:node.val
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        if not root:
            return
        level = [(root, 0)]
        res = []
        leftmost, rightmost = 0, 0
        mp = defaultdict(list)
        while level:
            nextLevel = []
            for pair in level:
                node, width = pair
                leftmost = min(leftmost, width)
                rightmost = max(rightmost, width)
                mp[width].append(node.val)
                if node.left:
                    nextLevel.append((node.left, width-1))
                if node.right:
                    nextLevel.append((node.right, width+1))
            level = nextLevel
        
        # for i in range(leftmost, rightmost+1):
        res = [mp[i] for i in range(leftmost, rightmost+1)]
        return  res
            
                    
