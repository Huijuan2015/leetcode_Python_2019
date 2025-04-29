# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #o(nlogn)
        if not root:
            return 0
        numLeftNodes = self.totalNodes(root.left) + 1
        if numLeftNodes > k:
            return self.kthSmallest(root.left, k)
        elif numLeftNodes < k:
            return self.kthSmallest(root.right, k-numLeftNodes)
        else:
            return root.val
        
    def totalNodes(self, root):
        if not root:
            return 0
        return self.totalNodes(root.left) + self.totalNodes(root.right) + 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #O(n)
        self.count = 0
        self.result = 0
        self.inorderTravese(root, k)
        return self.result
    
    def inorderTravese(self, node, k):
        if not node or self.count >= k:
            return
        self.inorderTravese(node.left, k)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self.inorderTravese(node.right, k)
