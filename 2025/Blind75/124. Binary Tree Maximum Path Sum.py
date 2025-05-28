# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    #     	每个节点的最大路径和可能包括：
	# •	仅自己 node.val
	# •	自己 + 左子树
	# •	自己 + 右子树
	# •	自己 + 左子树 + 右子树（这个不能往上传，只能作为局部最优路径）
        self.ans = float('-inf')
        
        def dfs(root):
            if not root:
                return 0
            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)
            self.ans = max(self.ans, l+r+root.val)
            # 返回当前节点的最大贡献值（只能选一边向上传）
            return max(l, r) + root.val
        
        dfs(root)
        return self.ans
        
