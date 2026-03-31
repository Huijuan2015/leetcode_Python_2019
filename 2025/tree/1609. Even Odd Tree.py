# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 用queue的话就加上size， 只处理当前层size
        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()
                val = node.val
                if level % 2 == 0: #even: 数字是奇数， 递增
                    if val % 2 == 0:
                        return False
                    if prev and val <= prev:
                        return False
                else:
                    if val %2 != 0:
                        return False
                    if prev and val >= prev:
                        return False
                prev = val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True

        


