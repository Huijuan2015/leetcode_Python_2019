# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        rootidx = inorder.index(root.val)
    
        leftIn = inorder[:rootidx]
        rightIn = inorder[rootidx+1:]
        leftPre = preorder[1:1+len(leftIn)]
        rightPre = preorder[1+len(leftIn):]
        
        root.right = self.buildTree(rightPre, rightIn)
        root.left = self.buildTree(leftPre, leftIn)
        return root

//cleaner
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        leftIn = inorder[:idx]
        rightIn = inorder[idx+1:]
        root.left = self.buildTree(preorder, leftIn)
        root.right = self.buildTree(preorder, rightIn)

        return root