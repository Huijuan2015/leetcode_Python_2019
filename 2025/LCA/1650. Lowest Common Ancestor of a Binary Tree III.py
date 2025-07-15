"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        # 好像两个不同长度的链表，通过“走完对方的长度”来 对齐长度。最终两个指针一定会在交点（即 LCA）相遇。
        a, b = p, q
        while a != b: #
            a = a.parent if a else q
            b = b.parent if b else p
        return a


        """
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p_parents = set()
        while p:
            p_parents.add(p)
            p = p.parent
        while q:
            if q in p_parents:
                return q
            q = q.parent
        return root