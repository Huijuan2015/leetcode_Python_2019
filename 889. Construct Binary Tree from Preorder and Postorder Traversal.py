# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return
        root = TreeNode(pre.pop(0))
        post.pop()
        if not pre:
            return root
        idx = post.index(pre[0])

        leftPost = post[:idx+1]
        rightPost = post[idx+1:]
        
        leftPre = pre[:idx+1]
        rightPre = pre[idx+1:]
        
        root.left = self.constructFromPrePost(leftPre, leftPost)
        root.right = self.constructFromPrePost(rightPre, rightPost)
        return root