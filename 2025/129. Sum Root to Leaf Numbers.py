# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #bfs
        if not root:
            return 0
        res = 0
        queue = deque([(root, root.val)])
        while queue:
            node, num = queue.popleft()
            if not node.left and not node.right:
                res += num
            if node.left:
                queue.append((node.left, num*10+node.left.val))
            if node.right:
                queue.append((node.right, num*10+node.right.val))
            
        return res
