# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        rootIdx = inorder.index(root.val)

        leftIn = inorder[:rootIdx]
        rightIn = inorder[rootIdx+1:]
        
        leftPost = postorder[:len(leftIn)]
        rightPost = postorder[len(leftIn):] #last one already popped
        
        root.left = self.buildTree(leftIn, leftPost)
        root.right = self.buildTree(rightIn, rightPost)
        return root
        
        