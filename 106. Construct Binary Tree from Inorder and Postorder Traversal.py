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
        
        
// cleaner
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
            return
        root = TreeNode(postorder.pop())
        
        idx = inorder.index(root.val)
        leftIn = inorder[:idx]
        
        rightIn = inorder[idx+1:]

        right = self.buildTree(rightIn, postorder) #要先递归right， 因为right在后续靠后
        left = self.buildTree(leftIn, postorder)

       
        root.right = right
        root.left = left
        return root