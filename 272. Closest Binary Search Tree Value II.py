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
        smallers, largers = [], []
        # smallers: 比target小的数， ----> 从小到大
        # largers: 比target大的数，  <---- 从小到大  ----> 从大到小
        res = []
        # put nodes into these 2 stks
        curr = root
        while curr:
            if curr.val < target:
                smallers.append(curr)
                curr = curr.right
            else:
                largers.append(curr)
                curr = curr.left
                
        # use inOrder to get next node
        def getSmaller(stk): 
            # push curr left branch to stack
            #找比当前node最大的最小值->左孩子的最右边
            s = stk.pop()
            curr = s.left
            while curr:
                stk.append(curr)
                curr = curr.right
            return s
        
        def getLarger(stk):
            # push curr right branch to stack
            #找比当前node最小的最大值->右孩子的最左边
            l = stk.pop()
            curr = l.right
            while curr:
                stk.append(curr)
                curr = curr.left
            return l
        
        while k:
            # s = smallers[-1] if smallers else None
            # l = largers[-1] if largers else None
            if smallers and (not largers or (largers and target - smallers[-1].val < largers[-1].val-target)): # use smaller
                res.append(getSmaller(smallers).val)
            else:
                res.append(getLarger(largers).val)
            k -= 1
        return res
            
        
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


O(log(n) + k) 
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


