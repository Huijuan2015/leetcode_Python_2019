# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #iterative
        if not root:
            return []
        res = []
        stk = []
        
        while stk or root:
            if root:
                stk.append(root)
                root = root.left
            else:
                node = stk.pop()
                res.append(node.val)
                root = node.right
        return res


        //////// with flag ---BEST!
        ret, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ret.append(node.val)
                    continue
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
        return ret

#         res = []
        
#         self.helper(root,res)
        
#         return res
    
#     def helper(self,root,arr):
#         if not root:
#             return
#         self.helper(root.left, arr)
#         arr.append(root.val)
#         self.helper(root.right,arr)
       
        
        