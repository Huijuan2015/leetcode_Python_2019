# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
         题意是说每个结点的右子树要么为空, 要么一定有一个左子树孩子和一个右子树孩子, 因此树的形状是左偏的. 
         所以我们要将最左边的子树作为最终的新根结点, 然后递归的将其 父结点作为其 右孩子,并且 父结点的右孩子 作为其 左孩子. 
         一个非常重要的地方是每次一定要将父结点的左右孩子都置为空, 因为父结点设置成其左孩子的右孩子之后成了叶子结点, 需要将其指针断掉.

        if not root or (not root.left and not root.right):
            return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return left