# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        curr = root
        while curr:
            self.stk.append(curr)
            curr = curr.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.stk:
            return 
        top = self.stk.pop()
        
        if top.right:
            curr = top.right
            while curr:
                self.stk.append(curr)
                curr = curr.left
        return top.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stk != [] # len(stk) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()