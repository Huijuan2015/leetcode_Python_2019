# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.res = root.val
        self.helper(root, target)
        return self.res
    
    def helper(self, root, target):
        
        if not root:
            return
        if abs(root.val-target) < abs(self.res-target):
            self.res = root.val
        if target > root.val:
            self.helper(root.right, target)
        else:
            self.helper(root.left, target)
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return
        q = collections.deque()
        minDist = float('inf')
        res = None
        q.append((root, abs(root.val-target)))
        
        while q:
            node, dist = q.popleft()
            if minDist > dist:
                minDist = dist
                res  = node.val
            if node.left and target < node.val:
                q.append((node.left, abs(node.left.val-target)))
            if node.right and target > node.val:
                q.append((node.right, abs(node.right.val-target)))
        return res
    
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    node = TreeNode(None)
    min = float('inf')
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        if not root:
            return
        tmp = abs(root.val-target)
        print root.val, tmp, self.min
        if tmp <= self.min:
            self.node = root
            self.min = tmp
        如果target比root大，结果只可能在右子树。所以可以二分一下
        self.closestValue(root.right, target)
        self.closestValue(root.left, target)
        return self.node.val


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    node = TreeNode(None)
    min = float('inf')
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        if not root:
            return
        tmp = abs(root.val-target)
        print root.val, tmp, self.min
        if tmp <= self.min:
            self.node = root
            self.min = tmp
        if target >= root.val:
            self.closestValue(root.right, target)
        else:
            self.closestValue(root.left, target)
        return self.node.val