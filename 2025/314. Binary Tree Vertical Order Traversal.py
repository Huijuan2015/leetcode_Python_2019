# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        col_dict = defaultdict(list)  # 记录每一列的结果
        queue = deque([(root, 0)])    #初始deque一个list, 其中元素格式是pair（x,y） 

        min_col = max_col = 0

        while queue:
            node, col = queue.popleft()
            if node:
                col_dict[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
        return [col_dict[x] for x in range(min_col, max_col+1)]