class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(n, 1, k, [])
        return self.res
    def helper(self, n, start, k, path):
        if k == 0:
            self.res.append(path)
            return
        for i in range(start, n+1):
            self.helper(n, i+1, k-1, path+[i



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #queue
        # if not q and not p:
        #     return True
        level = [(p, q)]
        
        while level:
            nextLevel = []
            
            for pair in level:
                p, q  = pair
                # print p.val, q.val
                if not p and not q:
                    continue #can't break
                if not p or not q or p.val != q.val:
                    return False
                nextLevel.append((p.left, q.left))
                nextLevel.append((p.right, q.right))
            level = nextLevel
        return True
        