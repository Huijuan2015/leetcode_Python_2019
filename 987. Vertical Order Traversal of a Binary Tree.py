# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #二维hashmap
        import collections
        mp = collections.defaultdict(lambda:collections.defaultdict(list))
        q = collections.deque()
        q.append((root, 0, 0))
        res = []
        while q:
            node, width, depth  = q.popleft()
            mp[width][depth].append(node.val)
            if node.left:
                q.append((node.left, width-1, depth+1))
            if node.right:
                q.append((node.right, width+1, depth+1))
        for width in sorted(mp):
            print mp[width]
            # {0: [1], 2: [5, 6]}
            tmp = []
            for depth in sorted(mp[width]): # nodes[i] nodes[i+1]
                print mp[width][depth]
                # [1]
                # [5, 6]
                tmp.extend(sorted(val for val in mp[width][depth]))
            res.append(tmp)     
        return res