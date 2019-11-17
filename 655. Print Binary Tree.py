首先应该算出二叉树的最大深度，直接写一个子函数返回这个最大深度，从而计算出宽度。
下面就是要遍历二叉树从而在数组中加入结点值。
我们先来看第一行，由于根结点只有一个，所以第一行只需要插入一个数字，不管这一行多少个位置，我们都是在最中间的位置插入结点值。
下面来看第二行，我们仔细观察可以发现，如果我们将这一行分为左右两部分，那么插入的位置还是在每一部分的中间位置，
这样我们只要能确定分成的部分的左右边界位置，就知道插入结点的位置了，
所以应该是使用分治法的思路。
在递归函数中，如果当前node不存在或者当前深度超过了最大深度直接返回，否则就给中间位置赋值为结点值，
然后对于左子结点，范围是左边界到中间位置，调用递归函数，注意当前深度加1；
同理对于右子结点，范围是中间位置加1到右边界，调用递归函数，注意当前深度加1，

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.getHeight(root)
        w = pow(2,h)-1
        self.res = [["" for i in range(w)] for j in range(h)]
        self.printHelper(root, 0, w-1, 0, h)
        return self.res
    
    def printHelper(self, node, i, j , currH, height): # i,j 区间
        if not node or currH == height: # == return: h: 0~h-1
            return
        nodePos = (i+j)/2
        self.res[currH][nodePos] = str(node.val)
        self.printHelper(node.left, i, nodePos, currH+1, height)
        self.printHelper(node.right, nodePos+1, j, currH+1, height)
        
    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right))+1