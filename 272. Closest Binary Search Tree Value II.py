# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ans = []
        # similar to 1, n space n
        def helper(root, target):
            if not root:
                return
            ans.append(root.val)

            # if root.val < target:
            helper(root.left, target)
            # else:
            helper(root.right, target)
                
        
        helper(root, target)
        return  sorted(ans, key=lambda x: abs(x - target))[:k]
        
        

queue
from collections import deque

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        self.q = deque()
        self.closestHelper(root)
        
        while len(self.q) > k:
            if abs(self.q[0] - target) > abs(self.q[-1] - target):
                self.q.popleft()
            else:
                self.q.pop()
                
        return list(self.q)
        
    def closestHelper(self, root: TreeNode):
        if not root:
            return
        
        self.closestHelper(root.left)
        self.q.append(root.val)
        self.closestHelper(root.right)


2 stack, K + Ologn?
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = []
        smallers, largers = [], []  # two stacks tracking smaller and larger nodes
        while root:
            if root.val > target:
                largers.append(root)
                root = root.left
            else:
                smallers.append(root)
                root = root.right
        # print smallers, largers 
        for _ in range(k):
            print target - smallers[-1].val, largers[-1].val - target
            if smallers and (not largers or largers and target - smallers[-1].val <= largers[-1].val - target):
                res.append(self._predecessor(smallers))
            else:
                res.append(self._successor(largers))
        return res

    def _predecessor(self, smallers):
        curr = smallers.pop()
        node = curr.left
        while node:
            smallers.append(node)
            node = node.right
        return curr.val

    def _successor(self, largers):
        curr = largers.pop()
        node = curr.right
        while node:
            largers.append(node)
            node = node.left
        return curr.val


