# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret, stk = [], [(root, False)]
        while stk:
            node, visited = stk.pop()
            if visited:
                ret.append(node.val)
            else:
                stk.append((node, True))
                if node.right:
                    stk.append((node.right, False))
                if node.left:
                    stk.append((node.left, False))
        return ret

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left,False))
        return ret
#         res = []
#         self.helper(root,res)
#         return res
    
#     def helper(self,root,arr):
#         if not root:
#             return
#         self.helper(root.left, arr)
#         self.helper(root.right,arr)
#         arr.append(root.val)
        
    


