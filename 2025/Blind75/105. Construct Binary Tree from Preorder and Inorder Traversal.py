# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        # find preorder in inorder
        # mp = {u:i for i, u in enumerate(inorder)}
        # root_idx = mp[root.val]
        root_idx = inorder.index(preorder[0])
        left_in = inorder[:root_idx]
        right_in = inorder[root_idx+1:]
        left_pre = preorder[1:root_idx+1]
        right_pre = preorder[root_idx+1:]
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        rootidx = inorder.index(root.val)

        leftinorder = inorder[:rootidx]
        rightinorder = inorder[rootidx+1:]

        leftpreorder = preorder[1:1+len(leftinorder)]
        rightpreorder = preorder[1+len(leftinorder):]

        root.right = self.buildTree(rightpreorder, rightinorder)
        root.left = self.buildTree(leftpreorder, leftinorder)

        return root
