# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # level order?
        # 建立与每个点相邻的map : 5:[6,2,3]
        # 然后 while K: for queue, append, 有重复所有需要visited记录
        # nodes left in k is ans
        from collections import defaultdict 
        from collections import deque 
        res = []
        mp = defaultdict(list) # node: node list
        q = deque()
        q.append(root)
        visited = set()  
        while q:
            node = q.popleft()
            if node.left:
                mp[node].append(node.left)
                mp[node.left].append(node)
                q.append(node.left)
            if node.right:
                mp[node].append(node.right)
                mp[node.right].append(node)
                q.append(node.right)

        level = [target]
        while K>0 and level:
            nextLevel = [] #node list
            for node in level:
                if node not in visited:
                    visited.add(node)
                    # 推进去的孩子也要是not visited，不然有重复
                    for nextNode in mp[node]:
                        if nextNode not in visited:
                            nextLevel.append(nextNode)
            level = nextLevel
            K-=1
        res = [node.val for node in level]
        return res
            