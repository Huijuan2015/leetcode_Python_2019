# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = collections.deque()
        res = 0
        q.append((root, 1))
        while q:
            node,length = q.popleft()
            res = max(res, length)
            if node.left:
                if node.val == node.left.val - 1:
                    q.append((node.left, length+1))
                else:
                    q.append((node.left, 1))
            if node.right:
                if node.val == node.right.val - 1:
                    q.append((node.right, length+1))
                else:
                    q.append((node.right, 1))
        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, None, 0)
        
    def helper(self, root, parent, length):
        if root is None:
            return length
        isCon = (parent is not None and root.val==parent+1)
        length = length+1 if isCon else 1
        return max(length, self.helper(root.left, root.val, length), self.helper(root.right, root.val, length))
    
            