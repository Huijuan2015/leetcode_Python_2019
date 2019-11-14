# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ret, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ret.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return ret

        #iteratively / stack
        if not root:
            return []
        stk = [root]
        res = []
        while stk:
            curr = stk.pop()
            if curr:
                res.append(curr.val)
                stk.append(curr.right)
                stk.append(curr.left)


#         res = []
#         self.helper(root,res)
#         return res

#     def helper(self, root, res):
#         if not root:
#             return
#         res.append(root.val)
#         self.helper(root.left, res)
#         self.helper(root.right, res)