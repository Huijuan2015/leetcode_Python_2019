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
    #     1.	从节点 p 开始，一直往上走，把所有父节点记录到一个集合 visited
	# 2.	从节点 q 开始，一直往上走
        visited = set()
        while p:
            visited.add(p)
            p = p.parent
        while q:
            if q in visited:
                return q
            q = q.parent
        return None
            
